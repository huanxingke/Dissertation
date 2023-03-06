import base64
import time
import json
import os
import re

import streamlit as st

from components.CookieManager import JSCookieManager
from utils.queryChemicals import QueryChemicals
from utils.initUserConfig import initUserConfig
from utils.chemicalsCard import chemicalsCard
from utils.refreshPage import refreshPage
from utils.config import menu_items


@st.cache(allow_output_mutation=True)
def load_chemicals():
    with open(os.path.join(st.session_state.work_path, "Data", "JsonFiles", "chemicals.json"), "r") as fp:
        chemicals_data = json.load(fp)
    return chemicals_data


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="常见危险化学品", page_icon="🧪", layout="wide", menu_items=menu_items)
st.markdown("### 🧪 常见危险化学品")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    with st.spinner("正在载入化学品数据..."):
        chemicals = load_chemicals()
        qc = QueryChemicals(chemicals=chemicals)
    if chemicals:
        # st.write(st.session_state)
        st.radio(
            "选择检索方式",
            ("关键词检索", "全部化学品", "查看已收藏"),
            horizontal=True,
            key="chemicals_query_mode"
        )
        if st.session_state.get("chemicals_query_mode") == "全部化学品":
            # 从 session_state 读取选项
            option = st.session_state.get("chemicals_all_option")
            option_index = 0
            if option:
                option_index = int(option.split("@")[0]) - 1
            st.selectbox(
                "全部化学品",
                [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(chemicals)],
                key="chemicals_all_option",
                index=option_index
            )
            chemicalsCard(chemicals[option_index])
        elif st.session_state.get("chemicals_query_mode") == "查看已收藏":
            # 检索是否存在收藏
            if st.session_state.get("chemical_favorites"):
                # 恢复为收藏列表
                chemical_favorites = st.session_state.get("chemical_favorites").split(",")
                chemical_favorites_list = []
                for chemical_index in chemical_favorites:
                    chemical_favorites_list.append(chemicals[int(chemical_index)])
                # 从 session_state 读取选项
                option = st.session_state.get("chemical_favorites_option")
                option_index = 0
                if option:
                    option_index = int(option.split("@")[0]) - 1
                st.selectbox(
                    "已收藏化学品",
                    [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(chemical_favorites_list)],
                    key="chemical_favorites_option",
                    index=option_index
                )
                chemicalsCard(chemical_favorites_list[option_index])
            else:
                st.warning("无收藏！")
        else:
            if st.session_state.get("chemicals_query_items"):
                keywords = st.text_input(
                    label="请输入要检索的化学品：",
                    placeholder=st.session_state.get("chemicals_query_items").get("keywords")
                )
            else:
                keywords = st.text_input(label="请输入要检索的化学品：")
            start_query = st.button("搜索")
            if start_query:
                with st.spinner("正在搜索..."):
                    if not keywords:
                        keywords = st.session_state.get("chemicals_query_items").get("keywords")
                    # 如果是 CAS 号则精确查询
                    if keywords.replace("-", "").isdigit():
                        query_chemicals = [i for i in chemicals if keywords in i["cas_number"]]
                    # 否则模糊匹配
                    else:
                        query_chemicals = qc.query(keywords=keywords)
                    if query_chemicals:
                        # 尝试保存本次搜索记录
                        with st.spinner("正在保存检索记录"):
                            # 拼接列表
                            query_chemicals_string = ",".join([str(i["index"]) for i in query_chemicals])
                            # 保存于 -> 应用会话
                            chemicals_query_items = {
                                "keywords": keywords,
                                "result": [i["index"] for i in query_chemicals]
                            }
                            st.session_state.chemicals_query_items = chemicals_query_items
                            # 保存于 -> 本地
                            JSCookieManager(key="chemicals_query_items", value=json.dumps(chemicals_query_items))
                            # 保存于 -> 云端
                            if st.session_state.get("jgy") is not None:
                                st.session_state.jgy.set(param="chemicals_query_items", value=json.dumps(chemicals_query_items))
                            option = st.selectbox(
                                f"【{keywords}】的搜索结果如下",
                                [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(query_chemicals)],
                                key="chemicals_query_option"
                            )
                            option_index = int(option.split("@")[0]) - 1
                            chemicalsCard(query_chemicals[option_index])
                    else:
                        st.warning("无搜索结果！")
            elif st.session_state.get("chemicals_query_items"):
                # 恢复为查询结果列表
                query_chemicals_index = st.session_state.get("chemicals_query_items").get("result")
                query_chemicals = []
                for query_chemical_index in query_chemicals_index:
                    query_chemicals.append(chemicals[query_chemical_index])
                # 从 session_state 读取选项
                option = st.session_state.get("chemicals_query_option")
                option_index = 0
                if option:
                    option_index = int(option.split("@")[0]) - 1
                option = st.selectbox(
                    f"【{st.session_state.get('chemicals_query_items').get('keywords')}】的搜索结果如下",
                    [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(query_chemicals)],
                    key="chemicals_query_option"
                )
                chemicalsCard(query_chemicals[option_index])
