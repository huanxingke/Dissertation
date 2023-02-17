import base64
import json

import streamlit as st

from utils.actionButton import addActionButton


def showActionInfo():
    # 从应用会话中获取坚果云类实例
    jgy = st.session_state.get("jgy")
    # 从应用会话中获取用户个人信息
    userinfo = st.session_state.get("userinfo")

    # 如果已实例化坚果云类
    # 那么就从云端获取所有数据
    if jgy is not None:
        # 应用会话 -> 没有个人信息 -> 获取个人信息
        if userinfo is None:
            cloud_userinfo = jgy.get("userinfo")
            if cloud_userinfo and cloud_userinfo.get("code") == 200:
                userinfo = json.loads(base64.b64decode(cloud_userinfo["value"]).decode())
                st.session_state.userinfo = userinfo

    # 右上角显示名字
    if userinfo is not None:
        show_name = userinfo["student_name"] if len(userinfo["student_name"]) > 3 else f"{userinfo['student_name'][0]}*{userinfo['student_name'][-1]}"
        addActionButton(action_id="userinfo-action", action_text=f"欢迎，{show_name}", action_href="./个人信息")
    else:
        addActionButton(action_id="userinfo-action", action_text="欢迎，游客", action_href="./个人信息")

    # 右上角显示坚果云连接状态
    if jgy is not None:
        addActionButton(action_id="jgy-action", action_text="【云√】", action_color="green", action_href="./首页")
    else:
        addActionButton(action_id="jgy-action", action_text="【云×】", action_color="orange", action_href="./首页")

    # 注销按钮
    addActionButton(action_id="exit-action", action_text="【注销】", action_color="red", action_func="clearAllCookie();")
