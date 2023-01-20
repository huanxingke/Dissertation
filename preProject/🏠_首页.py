import streamlit as st
import requests

from components.CookieManager import CookieManager


# -------------------- 页眉 -------------------- #
# 页面设置
st.set_page_config(page_title="首页", page_icon="🏠")
# 页面标题线
header = st.header("🏠 首页")
username = st.session_state.get("username")
if username:
    subheader = st.subheader(f"欢迎🎉 {username}")
# 分割线
st.markdown("---")


# -------------------- README.md -------------------- #
@st.cache
def getREADME():
    readme_url = "https://rawcdn.githack.com/huanxingke/Dissertation/275477ae504f415e87935db3e1dd242fd8af32e8/README.md"
    readme = requests.get(url=readme_url).text
    return readme


markdown_readme = getREADME()
st.markdown(markdown_readme)