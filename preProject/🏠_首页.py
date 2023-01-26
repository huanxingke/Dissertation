import os

import streamlit as st
import requests

from components.CookieManager import CookieManager
from utils.page_header import pageHeader


# -------------------- cookie 管理器 -------------------- #
cookie_manager = CookieManager()

# -------------------- 页眉 -------------------- #
# 页面设置
st.set_page_config(page_title="首页", page_icon="🏠")
pageHeader(header_value="🏠 首页", cookie_manager=cookie_manager)


# -------------------- README.md -------------------- #
@st.cache
def getREADME():
    readme_url = "https://raw.githubusercontent.com/huanxingke/Dissertation/master/README.md"
    readme = requests.get(url=readme_url).text.strip()
    return readme


with st.spinner("Loading ReadMe.md..."):
    markdown_readme = getREADME()
    st.markdown(markdown_readme)


if os.path.exists("123.txt"):
    with open("123.txt", "r") as fp:
        st.write(fp.read())
else:
    with open("123.txt", "w") as fp:
        fp.write("123")