import base64
import os

import streamlit as st

from utils.initUserConfig import initUserConfig
from utils.config import menu_items


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="知识学习模块", page_icon="📖", layout="wide", menu_items=menu_items)
st.markdown("### 📖 知识学习模块")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    with open(os.path.join(st.session_state.work_path, "Data", "Knowledge", "EnterpriseQValue.md"), "r", encoding="utf-8") as fp:
        knowledge = fp.read()
    with open(os.path.join(st.session_state.work_path, "Data", "Knowledge", "pictures", "EnvironmentalParameterDetection", "噪声危害一览表.png"), "rb") as fp:
        img = base64.b64encode(fp.read()).decode()
    knowledge += f"""
    [Image1]:data:image/png;base64,{img}\n\n
    """
    st.markdown(knowledge)