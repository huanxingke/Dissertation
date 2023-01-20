import streamlit as st


# -------------------- 页眉 -------------------- #
def pageHeader(header_value, cookie_manager, subheader_value=None):
    # 用户名
    username = None
    username_cookie = cookie_manager.get("username")
    if username_cookie and username_cookie.get("code") == 200:
        username = username_cookie.get("value")
    # 页面标题
    header = st.header(header_value)
    # 页面副标题
    subheader = None
    if username:
        subheader = st.subheader(f"欢迎🎉 {username}")
    elif subheader_value:
        subheader = st.subheader(subheader_value)
    # 分割线
    st.markdown("---")
    return header, subheader, username