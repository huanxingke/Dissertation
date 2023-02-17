import streamlit as st

from utils.actionButton import addActionButton


def showActionInfo():
    jgy = st.session_state.get("jgy")
    userinfo = st.session_state.get("userinfo")
    if userinfo is not None:
        addActionButton(action_id="userinfo-action", action_text=f"{userinfo['student_name']}，欢迎您！", action_href="./个人信息")
    else:
        addActionButton(action_id="userinfo-action", action_text="游客，欢迎您！", action_href="./个人信息")
    if jgy is not None:
        addActionButton(action_id="jgy-action", action_text="【坚果云已连接】", action_color="orange", action_href="./首页")
    else:
        addActionButton(action_id="jgy-action", action_text="【坚果云未连接】", action_color="orange", action_href="./首页")
    addActionButton(action_id="exit-action", action_text="【注销】", action_color="red", action_func="clearAllCookie();")
