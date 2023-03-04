import base64
import time
import json
import os

import streamlit as st

from utils.queryChemicals import QueryChemicals
from utils.initUserConfig import initUserConfig
from utils.chemicalsCard import chemicalsCard
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
        keywords = st.text_input("关键词", key="keywords_input")
        if st.button("搜索", key="query_start"):
            with st.spinner("正在搜索..."):
                query_chemicals = qc.query(keywords=keywords)
            if query_chemicals:
                if len(query_chemicals) > 0:
                    chemicals_with_pic = []
                    path = os.path.join(st.session_state.work_path, "Data", "Images", "struct_pic", "{}.png")
                    for query_chemical in query_chemicals:
                        struct_pic = ""
                        cas_number = query_chemical["cas_number"]
                        if os.path.exists(path.format(cas_number)):
                            with open(path.format(cas_number), "rb") as fp:
                                struct_pic = "data:image/png;base64," + base64.b64encode(fp.read()).decode()
                        query_chemical["struct_pic"] = struct_pic
                    chemicalsCard(query_chemicals)
                else:
                    st.warning("无搜索结果")