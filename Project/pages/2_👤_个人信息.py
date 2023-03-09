import base64
import time
import json
import os

import streamlit as st

from components.CookieManager import CookieManager, JSCookieManager

from utils.config import menu_items
from utils.refreshPage import refreshPage
from utils.actionButton import addActionButton
from utils.initUserConfig import initUserConfig


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="个人信息", page_icon="👤", layout="wide", menu_items=menu_items)
st.markdown("### 👤 个人信息")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    # 1.尝试 -> 应用会话 -> 获取坚果云类实例
    jgy = st.session_state.get("jgy")
    # 2.尝试 -> 应用会话 -> 获取用户个人信息
    userinfo = st.session_state.get("userinfo")

    # 3.如果 -> 不存在用户个人信息 -> 显示输入界面
    if userinfo is None:
        with st.form("userinfo_form"):
            student_name = st.text_input(label="姓名：", key="student_name")
            student_email = st.text_input(label="邮箱：", key="student_email")
            student_school = st.text_input(label="学校：", key="student_school")
            student_number = st.text_input(label="学号：", key="student_number")
            student_major = st.text_input(label="专业：", key="student_major")
            student_class = st.text_input(label="班级：", key="student_class")
            student_teacher_name = st.text_input(label="指导老师：", key="student_teacher_name")
            confirm = st.form_submit_button("确定")
            if confirm:
                userinfo = {
                    "student_name": student_name,
                    "student_email": student_email,
                    "student_school": student_school,
                    "student_number": student_number,
                    "student_major": student_major,
                    "student_class": student_class,
                    "student_teacher_name": student_teacher_name
                }
                # 4.保存 -> 应用会话 -> 用户个人信息
                st.session_state.userinfo = userinfo
                # 5.保存 -> 本地 -> 用户个人信息
                JSCookieManager(key="userinfo", value=json.dumps(userinfo))
                # 6.尝试 -> 保存 -> 云端 -> 用户个人信息
                if jgy is not None:
                    with st.spinner("正在同步个人信息至云端..."):
                        upload_res = jgy.set(param="userinfo", value=json.dumps(userinfo))
                        if upload_res.get("code") == 200:
                            st.success("已同步个人信息至云端！")
                        else:
                            st.error(f"同步个人信息至云端失败: {upload_res['error']}")
                else:
                    st.success("已储存个人信息至浏览器本地！")
                # 7.右上角显示 -> 名字
                show_name = userinfo["student_name"] if len(
                    userinfo["student_name"]) <= 3 else f"{userinfo['student_name'][0]}*{userinfo['student_name'][-1]}"
                addActionButton(action_id="userinfo-action", action_text=show_name, action_href="./个人信息")
    # 3.如果 -> 存在用户个人信息 -> 显示个人信息数据
    else:
        st.markdown(f"**姓名**：{userinfo['student_name']}")
        st.markdown(f"**邮箱**：{userinfo['student_email']}")
        st.markdown(f"**学校**：{userinfo['student_school']}")
        st.markdown(f"**学号**：{userinfo['student_number']}")
        st.markdown(f"**专业**：{userinfo['student_major']}")
        st.markdown(f"**班级**：{userinfo['student_class']}")
        st.markdown(f"**指导老师**：{userinfo['student_teacher_name']}")
    # 最后都要加上清除按钮
    clear = st.button("清除个人信息")
    if clear:
        # 清除 -> 应用会话 -> 用户个人信息
        if st.session_state.get("userinfo"):
            del st.session_state.userinfo
        # 清除 -> 本地 -> 用户个人信息
        JSCookieManager(key="userinfo", delete=True)
        # 右上角显示
        addActionButton(action_id="userinfo-action", action_text="游客", action_href="./个人信息")
        # 尝试 -> 清除 -> 云端 -> 用户个人信息
        if jgy is not None:
            with st.spinner("正在删除云端个人信息..."):
                delete_res = jgy.delete("userinfo")
                if delete_res.get("code") == 200:
                    st.success("已删除云端信息！")
                    refreshPage()
                else:
                    st.error(f"删除云端信息失败！")