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
        select_mode = st.radio(
            "选择检索方式",
            ("关键词检索", "全部化学品", "查看已收藏"),
            horizontal=True
        )
        if select_mode == "全部化学品":
            option = st.selectbox(
                "全部化学品",
                [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(chemicals)]
            )
            option_index = int(option.split("@")[0]) - 1
            chemicalsCard(chemicals[option_index])
        elif select_mode == "查看已收藏":
            if st.session_state.get("chemical_favorites"):
                # 恢复为列表
                chemical_favorites = st.session_state.get("chemical_favorites").split(",")
                chemical_favorites_list = []
                for chemical_index in chemical_favorites:
                    chemical_favorites_list.append(chemicals[int(chemical_index)])
                option = st.selectbox(
                    "已收藏化学品",
                    [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(chemical_favorites_list)]
                )
                option_index = int(option.split("@")[0]) - 1
                chemicalsCard(chemical_favorites_list[option_index])
            else:
                st.warning("无收藏！")
        else:
            keywords = st.text_input(
                label="请输入要检索的化学品：",
                key="keywords_input",
                placeholder=st.session_state.get("query_chemicals_keywords") or ""
            )
            start_query = st.button("搜索", key="query_start")
            if start_query:
                with st.spinner("正在搜索..."):
                    if keywords.replace("-", "").isdigit():
                        query_chemicals = [i for i in chemicals if keywords in i["cas_number"]]
                    else:
                        query_chemicals = qc.query(keywords=keywords)
                    if query_chemicals:
                        # 尝试保存本次搜索记录
                        with st.spinner("正在保存检索记录"):
                            # 拼接列表
                            query_chemicals_string = ",".join([str(i["index"]) for i in query_chemicals])
                            # 保存于 -> 本地
                            JSCookieManager(key="query_chemicals", value=query_chemicals_string, nobase64=True)
                            JSCookieManager(key="query_chemicals_keywords", value=keywords, nobase64=True)
                            # 保存于 -> 云端
                            if st.session_state.get("jgy") is not None:
                                st.session_state.jgy.set(param="query_chemicals", value=query_chemicals_string,
                                                         nobase64=True)
                                st.session_state.jgy.set(param="query_chemicals_keywords", value=keywords,
                                                         nobase64=True)
                            if len(query_chemicals) > 1:
                                refreshPage()
                            else:
                                option = st.selectbox(
                                    f"【{keywords}】的搜索结果如下（唯一结果）",
                                    [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(query_chemicals)],
                                    disabled=True
                                )
                                option_index = int(option.split("@")[0]) - 1
                                chemicalsCard(query_chemicals[option_index])
                    else:
                        st.warning("无搜索结果！")
            elif st.session_state.get("query_chemicals"):
                # 恢复为列表
                query_chemicals = st.session_state.get("query_chemicals").split(",")
                query_chemicals_list = []
                for chemical_index in query_chemicals:
                    query_chemicals_list.append(chemicals[int(chemical_index)])
                option_title = f"【{st.session_state.get('query_chemicals_keywords')}】的搜索结果如下"
                option = st.selectbox(
                    option_title if len(query_chemicals_list) > 1 else option_title + "（唯一结果）",
                    [f"{i_index + 1}@ {i['name'][0]}" for i_index, i in enumerate(query_chemicals_list)],
                    disabled=True if len(query_chemicals_list) <= 1 else False
                )
                option_index = int(option.split("@")[0]) - 1
                chemicalsCard(query_chemicals_list[option_index])
