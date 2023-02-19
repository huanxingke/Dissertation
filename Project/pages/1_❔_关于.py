import os

import streamlit as st
import requests

from utils.initUserConfig import initUserConfig

# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="关于", page_icon="❔")
st.markdown("### ❔ 关于")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    # 加载 README.md
    with st.spinner("正在加载本站信息..."):
        readme_md = os.path.join(st.session_state.work_path, "README.md")
        with open(readme_md, "r", encoding="utf-8") as fp:
            st.markdown(fp.read())