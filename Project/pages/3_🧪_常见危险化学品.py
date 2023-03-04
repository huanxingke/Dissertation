import base64
import time
import json
import os

import streamlit as st

from utils.config import menu_items
from utils.initUserConfig import initUserConfig


@st.cache
def load_chemicals():
    with open(os.path.join(st.session_state.work_path, "Data", "jsonfiles", "chemicals.json"), "r") as fp:
        chemicals_data = json.load(fp)
    return chemicals_data


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="常见危险化学品", page_icon="🧪", menu_items=menu_items)
st.markdown("### 🧪 常见危险化学品")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #
    with st.spinner("正在载入化学品数据..."):
        chemicals = load_chemicals()
    if chemicals is not None:
        st.write(chemicals[0]["name"])