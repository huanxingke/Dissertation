import base64
import json
import os

import streamlit as st

from components.CookieManager import CookieManager, JSCookieManager
from components.Webdav import JianGuoYunClient
from utils.actionButton import addActionButton
from utils.footer import footer


# 每个页面打开时都需要初始化
def initUserConfig():
    def init():
        # ****** 0.网页底部文字更改 ****** #
        footer()

        # ****** 1.判断应用环境并选择路径 ****** #
        # 环境 -> 本地
        if os.environ.get("USERDOMAIN") == "HUANXINGKE":
            st.session_state.work_path = os.path.abspath(os.path.dirname(os.getcwd()))
        # 环境 -> 云端
        else:
            st.session_state.work_path = "."

        # ****** 2.获取所有本地 cookie ****** #
        # 尝试 -> 本地 -> 获取所有 cookie
        cookies = None
        cm = CookieManager()
        cookies_result = cm.getAll()
        if cookies_result and cookies_result.get("code") == 200:
            cookies = cookies_result["cookies"]
        else:
            return False

        # ****** 3.检查应用会话 ****** #
        # 尝试 -> 应用会话 -> 获取坚果云类实例
        jgy = st.session_state.get("jgy")
        # 尝试 -> 应用会话 -> 获取用户个人信息
        userinfo = st.session_state.get("userinfo")
        # 尝试 -> 应用会话 -> 获取用户收藏的化学品
        chemical_favorites = st.session_state.get("chemical_favorites")
        # 尝试 -> 应用会话 -> 获取用户最近一次搜索化学品的记录
        chemicals_query_items = st.session_state.get("chemicals_query_items")

        # ****** 4.先尝试自动连接坚果云 ****** #
        # 如果 -> 未连接坚果云
        if jgy is None:
            # 如果 -> 本地 -> 存在云盘配置
            if cookies is not None and cookies.get("user") is not None:
                user = json.loads(base64.b64decode(cookies.get("user")).decode())
                username = user["username"]
                password = user["password"]
                # 尝试 -> 连接云盘
                new_jgy = JianGuoYunClient(username=username, password=password)
                login_jgy = new_jgy.login()
                # 如果 -> 连接成功
                if login_jgy["code"] == 200:
                    jgy = new_jgy
                    # 保存 -> 应用会话 -> 坚果云配置
                    st.session_state.user = user
                    # 保存 -> 应用会话 -> 坚果云类实例
                    st.session_state.jgy = jgy
                # 如果 -> 连接失败
                else:
                    # 清除 -> 本地 -> 云盘配置
                    JSCookieManager(key="user", delete=True)

        # ****** 5.尝试获取用户的本地和云端数据 ****** #
        # 5.1.获取用户个人信息[以云端优先]
        # 5.1.1.[首先 -> 云端] 如果 -> 应用会话 -> 不存在用户个人信息
        if userinfo is None:
            # 如果 -> 已连接坚果云
            if jgy is not None:
                # 尝试 -> 云端 -> 获取用户个人信息
                cloud_userinfo = jgy.get("userinfo")
                # 如果 -> 获取成功
                if cloud_userinfo and cloud_userinfo.get("code") == 200:
                    userinfo = json.loads(base64.b64decode(cloud_userinfo["value"]).decode())
                    # 保存 -> 应用会话 -> 用户个人信息
                    st.session_state.userinfo = userinfo
                    # 保存 -> 本地 -> 用户个人信息
                    JSCookieManager(key="userinfo", value=json.dumps(userinfo))
        # 5.1.2.[其次 -> 本地] 如果 -> 应用会话 -> 仍不存在用户个人信息
        if userinfo is None:
            # 如果 -> 本地 -> 存在用户个人信息
            if cookies is not None and cookies.get("userinfo") is not None:
                userinfo = json.loads(base64.b64decode(cookies.get("userinfo")).decode())
                # 保存 -> 应用会话 -> 用户个人信息
                st.session_state.userinfo = userinfo
                # 如果 -> 已连接坚果云
                if jgy is not None:
                    # 尝试 -> 保存 -> 云端 -> 用户个人信息
                    jgy.set(param="userinfo", value=json.dumps(userinfo))

        # 5.2.同步用户收藏的化学品[以本地优先]
        # 5.2.1.[首先 -> 本地] 直接从本地获取并上传云端
        if cookies is not None and cookies.get("chemical_favorites") is not None:
            chemical_favorites = cookies.get("chemical_favorites")
            # 保存 -> 应用会话 -> 用户收藏的化学品
            st.session_state.chemical_favorites = chemical_favorites
            # 如果 -> 已连接坚果云
            if jgy is not None:
                # 尝试 -> 保存 -> 云端 -> 用户收藏的化学品
                jgy.set(param="chemical_favorites", value=chemical_favorites, nobase64=True)
        # 5.2.2.[其次 -> 云端] 丛云端获取并保存于本地
        if chemical_favorites is None:
            # 如果 -> 已连接坚果云
            if jgy is not None:
                # 尝试 -> 云端 -> 获取用户收藏的化学品
                cloud_chemical_favorites = jgy.get(param="chemical_favorites", nobase64=True)
                # 如果 -> 获取成功
                if cloud_chemical_favorites and cloud_chemical_favorites.get("code") == 200:
                    chemical_favorites = cloud_chemical_favorites["value"]
                    # 保存 -> 应用会话 -> 用户收藏的化学品
                    st.session_state.chemical_favorites = chemical_favorites
                    # 保存 -> 本地 -> 用户收藏的化学品
                    JSCookieManager(key="chemical_favorites", value=chemical_favorites, nobase64=True)

        # 5.3.获取用户最近一次搜索化学品的记录[以云端优先]
        # 5.3.1.[首先 -> 云端] 如果 -> 应用会话 -> 不存在用户个人信息
        if chemicals_query_items is None:
            # 如果 -> 已连接坚果云
            if jgy is not None:
                # 尝试 -> 云端 -> 获取用户最近一次搜索化学品的记录
                cloud_chemicals_query_items = jgy.get("chemicals_query_items")
                # 如果 -> 获取成功
                if cloud_chemicals_query_items and cloud_chemicals_query_items.get("code") == 200:
                    chemicals_query_items = json.loads(base64.b64decode(cloud_chemicals_query_items["value"]).decode())
                    # 保存 -> 应用会话 -> 用户最近一次搜索化学品的记录
                    st.session_state.chemicals_query_items = chemicals_query_items
                    # 保存 -> 本地 -> 用户最近一次搜索化学品的记录
                    JSCookieManager(key="chemicals_query_items", value=json.dumps(chemicals_query_items))
        # 5.3.2.[其次 -> 本地] 如果 -> 应用会话 -> 仍不存在用户最近一次搜索化学品的记录
        if chemicals_query_items is None:
            # 如果 -> 本地 -> 存在用户最近一次搜索化学品的记录
            if cookies is not None and cookies.get("chemicals_query_items") is not None:
                chemicals_query_items = json.loads(base64.b64decode(cookies.get("chemicals_query_items")).decode())
                # 保存 -> 应用会话 -> 用户最近一次搜索化学品的记录
                st.session_state.chemicals_query_items = chemicals_query_items
                # 如果 -> 已连接坚果云
                if jgy is not None:
                    # 尝试 -> 保存 -> 云端 -> 用户最近一次搜索化学品的记录
                    jgy.set(param="chemicals_query_items", value=json.dumps(chemicals_query_items))

        # ****** 6.网页右上角显示 ****** #
        # 6.1名字
        if userinfo is not None:
            show_name = userinfo["student_name"] if len(userinfo["student_name"]) <= 3 else f"{userinfo['student_name'][0]}*{userinfo['student_name'][-1]}"
            addActionButton(action_id="userinfo-action", action_text=show_name, action_href="./个人信息")
        else:
            addActionButton(action_id="userinfo-action", action_text="游客", action_href="./个人信息")
        # 6.2坚果云连接状态
        if jgy is not None:
            addActionButton(action_id="jgy-action", action_text="[云√]", action_color="green", action_href="./首页")
        else:
            addActionButton(action_id="jgy-action", action_text="[云×]", action_color="orange", action_href="./首页")
        # 6.3注销按钮
        addActionButton(action_id="exit-action", action_text="[注销]", action_color="red", action_func="clearAllCookie()")

        # ****** 7.返回初始化完成结果 ****** #
        return True

    with st.spinner("正在初始化页面..."):
        init_result = init()
        return init_result