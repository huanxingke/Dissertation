import streamlit as st
import requests

from components.StreamlitWSLocalstorage import injectWebsocketCode, getOrCreateUID
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

conn = injectWebsocketCode(hostPort='linode.liquidco.in', uid=getOrCreateUID())

st.write('setting into localStorage')
ret = conn.setLocalStorageVal(key='k1', val='v1')
st.write('ret: ' + ret)

st.write('getting from localStorage')
ret = conn.getLocalStorageVal(key='k1')
st.write('ret: ' + ret)