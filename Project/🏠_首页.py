"""
chemical-eps: Chemical Emergency Plan System
"""
import base64
import time
import json

import streamlit as st

from components.CookieManager import JSCookieManager
from components.Webdav import JianGuoYunClient

from utils.refreshPage import refreshPage
from utils.actionButton import addActionButton
from utils.initUserConfig import initUserConfig


# 断开云盘链接
def disconnect():
    # 从应用会话中移除
    if st.session_state.get("jgy"):
        del st.session_state.jgy
    if st.session_state.get("user"):
        del st.session_state.user
    # 从本地 cookie 中移除
    JSCookieManager(key="user", delete=True)
    addActionButton(action_id="jgy-action", action_text="【云×】", action_color="orange", action_href="./首页")
    # 刷新页面
    refreshPage()


# 展示云盘配置情况
def showUser():
    st.success("已成功连接至坚果云盘！")
    st.text_input(label="[坚果云]账户：", key="show_username", disabled=True, value=username)
    st.text_input(label="[坚果云]应用密码：", key="show_password", disabled=True, value=password, type="password")
    addActionButton(action_id="jgy-action", action_text="【云√】", action_color="green", action_href="./首页")
    if st.button("断开连接"):
        with st.spinner("正在断开连接..."):
            disconnect()


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="首页", page_icon="🏠")
st.markdown("### 🏠 首页")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    st.markdown("""
    - 由于Streamlit暂无原生的持久化储存api，\
    且课题要求不能使用自己部署的服务器，\
    因此本程序采用 cookie + 免费云盘[坚果云]云储存的方式进行数据储存。
    - 您可以**直接使用本程序**，但数据**只能保存于浏览器本地**。
    - 如需**云端储存**，请按以下教程开启[坚果云第三方应用授权**WebDAV**]：
    - [坚果云第三方应用授权WebDAV开启方法](https://help.jianguoyun.com/?p=2064)
    - 注：坚果云为目前国内最好用的支持webdav的云盘，且免费版每月有 1GB 上传和 3GB 下载流量，\
    足够本系统进行数据云储存，如果您本身也在用坚果云，建议另外注册一个坚果云账号以供本系统使用。
    """)

    # 1.尝试 -> 应用会话 -> 获取坚果云类实例
    jgy = st.session_state.get("jgy")
    # 2.如果 -> 已连接坚果云 -> 显示坚果云配置
    if jgy is not None:
        user = st.session_state.user
        username = user["username"]
        password = user["password"]
        showUser()
    # 2.如果 -> 未连接坚果云 -> 显示输入界面
    else:
        username = st.text_input(label="输入账号：", key="username")
        password = st.text_input(label="输入应用密码：", key="password", type="password")
        confirm = st.button("确定")
        if confirm:
            user = {
                "username": username,
                "password": password,
            }
            # 3.尝试 -> 连接坚果云
            new_jgy = JianGuoYunClient(username=username, password=password)
            login_jgy = new_jgy.login()
            # 4.如果 -> 连接成功
            if login_jgy["code"] == 200:
                # 5.保存 -> 应用会话 -> 坚果云配置
                st.session_state.user = user
                # 6.保存 -> 应用会话 -> 坚果云类实例
                st.session_state.jgy = jgy
                # 7.显示坚果云配置
                showUser()
                # 8.保存 -> 本地 -> 坚果云配置
                JSCookieManager(key="user", value=json.dumps(user))
                # 9.刷新页面
                refreshPage(alert="登录成功！点击刷新页面。")
            # 4.如果 -> 连接失败
            else:
                st.error(f"连接坚果云盘失败：{login_jgy['error']}")
                # 5.重置坚果云配置
                disconnect()
