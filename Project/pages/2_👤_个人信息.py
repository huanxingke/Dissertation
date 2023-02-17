import base64
import time
import json

import streamlit as st

from components.CookieManager import CookieManager, JSCookieManager, refreshPage
from utils.actionButton import addActionButton
from utils.showActionInfo import showActionInfo

# ---------- Start:每页基础配置 ---------- #
showActionInfo()
st.markdown("### 👤 个人信息")
# ---------- End:每页基础配置 ---------- #


# 同步个人信息至云端
def uploadUserInfo():
    with st.spinner("正在同步个人信息至云端..."):
        upload_res = jgy.set(param="userinfo", value=json.dumps(userinfo))
        if upload_res.get("code") == 200:
            st.success("已同步个人信息至云端！")
        else:
            st.error(f"同步个人信息至云端失败: {upload_res['error']}")


def showUserInfo():
    # 保存个人信息于应用会话
    st.session_state.userinfo = userinfo
    if not auto_input:
        # ** 保存数据于本地 ** #
        JSCookieManager(key="userinfo", value=json.dumps(userinfo))
        show_name = userinfo["student_name"] if len(userinfo["student_name"]) > 3 else f"{userinfo['student_name'][0]}*{userinfo['student_name'][-1]}"
        addActionButton(action_id="userinfo-action", action_text=f"欢迎，{show_name}", action_href="./个人信息")
        # ** 同步数据至云端 ** #
        if jgy is not None:
            uploadUserInfo()
        else:
            st.success("已储存个人信息至浏览器本地！")
    else:
        st.markdown(f"**姓名**：{student_name}")
        st.markdown(f"**邮箱**：{student_email}")
        st.markdown(f"**学校**：{student_school}")
        st.markdown(f"**学号**：{student_number}")
        st.markdown(f"**专业**：{student_major}")
        st.markdown(f"**班级**：{student_class}")
        st.markdown(f"**指导老师**：{student_teacher_name}")
        clear = st.button("清除个人信息")
        show_name = userinfo["student_name"] if len(userinfo["student_name"]) > 3 else f"{userinfo['student_name'][0]}*{userinfo['student_name'][-1]}"
        addActionButton(action_id="userinfo-action", action_text=f"欢迎，{show_name}", action_href="./个人信息")
        # ** 同步数据至云端 ** #
        if not cloud_input and jgy is not None:
            uploadUserInfo()
        # ** 保存数据于本地 ** #
        elif cloud_input:
            JSCookieManager(key="userinfo", value=json.dumps(userinfo))
        if clear:
            if st.session_state.get("userinfo"):
                del st.session_state.userinfo
            JSCookieManager(key="userinfo", delete=True)
            addActionButton(action_id="userinfo-action", action_text="欢迎，游客", action_href="./个人信息")
            if jgy is not None:
                with st.spinner("正在删除云端个人信息..."):
                    delete_res = jgy.delete("userinfo")
                    if delete_res.get("code") == 200:
                        st.success("已删除云端信息！")
                        refreshPage()
                    else:
                        st.error(f"删除云端信息失败！")


# ** 判断是否是自动填写 ** #
auto_input = False
# ** 判断是否是云端数据 ** #
cloud_input = False
# ** 初始化个人信息变量 ** #
userinfo = None

# 从云端获取数据
# 注: 所有数据优先以云端为准
jgy = st.session_state.get("jgy")
if jgy is not None:
    userinfo = jgy.get("userinfo")
    if userinfo and userinfo.get("code") == 200:
        cloud_input = True

# 从本地获取数据
if not cloud_input:
    # 实例化双向的 cookie 管理器
    cm = CookieManager()
    userinfo = cm.get("userinfo")

if userinfo and userinfo.get("code") == 200:
    auto_input = True
    userinfo = json.loads(base64.b64decode(userinfo["value"]).decode())
    student_name = userinfo["student_name"]
    student_email = userinfo["student_email"]
    student_school = userinfo["student_school"]
    student_number = userinfo["student_number"]
    student_major = userinfo["student_major"]
    student_class = userinfo["student_class"]
    student_teacher_name = userinfo["student_teacher_name"]
    showUserInfo()
else:
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
            showUserInfo()