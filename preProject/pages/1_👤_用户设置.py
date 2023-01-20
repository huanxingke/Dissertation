import re

import streamlit as st

from components.CookieManager import CookieManager
from utils.page_header import pageHeader


# -------------------- cookie 管理器 -------------------- #
cookie_manager = CookieManager()

# -------------------- 页眉 -------------------- #
# 页面设置
st.set_page_config(page_title="用户设置", page_icon="👤")
header, subheader, username = pageHeader(
    header_value="👤 用户设置", cookie_manager=cookie_manager, subheader_value="当前身份：游客🚶"
)

# -------------------- 用户设置 -------------------- #
if not username:
    username_input = st.text_input("您可以设置临时用户名:", placeholder="请输入用户名", key="input_username")
    if st.button("确认用户名", key="save_username"):
        if not "".join([re.sub(r"\s+", "", i) for i in username_input]):
            st.write("您还没有输入用户名!")
        else:
            cookie_manager.set("username", username_input)
else:
    username_input = st.text_input("您可以更改用户名:", placeholder="请输入用户名", key="input_change_username")
    if st.button("确认更改", key="change_username"):
        if not "".join([re.sub(r"\s+", "", i) for i in username_input]):
            st.write("您还没有输入用户名!")
        else:
            cookie_manager.set("username", username_input)
    if st.button("清除用户名", key="delete_username"):
        cookie_manager.delete("username")