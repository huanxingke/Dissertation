import streamlit as st


# -------------------- 页眉 -------------------- #
def pageHeader(header_value, subheader_value=None):
    # 设置应用会话
    if not st.session_state.get("cookie"):
        st.session_state.cookie = {}
    username = st.session_state.cookie.get("chemical-username")
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