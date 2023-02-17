"""
chemical-eps: Chemical Emergency Plan System
"""
import base64
import time
import json

import streamlit as st

from components.CookieManager import CookieManager, JSCookieManager, refreshPage
from components.Webdav import JianGuoYunClient
from utils.actionButton import addActionButton
from utils.showActionInfo import showActionInfo

# ---------- Start:每页基础配置 ---------- #
showActionInfo()
st.markdown("### 🏠 首页")
# ---------- End:每页基础配置 ---------- #


# 控制密码密/明文的脚本
def insertPasswordJS():
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
    </head>
    <body>
        <script>
            //新建按钮
            function createButton(label, id, beforeNode, func) {
                //防止重复创建
                if (root_document.find("#" + id).length > 0) {
                    root_document.find("#" + id).remove();
                }
                //开始新建
                var new_button = window.top.document.createElement("p");
                $(new_button).attr("kind", "primary");
                $(new_button).attr("class", button_css_style);
                $(new_button).attr("id", id);
                $(new_button).html(close_eye_svg);
                //绑定事件
                $(new_button).click(function(){
                    //执行函数
                    func();
                });
                beforeNode.after(new_button);
                return new_button;
            }

            //获取父节点
            var parent = $(window.frameElement).parent();
            //获取根文档
            var root_document = $(window.frameElement).parents("#root");
            //获取streamlit按钮
            var css_button = root_document.find("div.row-widget.stButton").find("button");
            var button_css_style = css_button.attr("class");
            //获取 password-input 元素
            var password_div = root_document.find("label:contains([坚果云]应用密码)").parent().parent();
            var password_input = password_div.find("input");
            
            //判断以上获取的元素是否存在, 不存在则刷新一下页面
            if (css_button.length == 0 || password_input.length == 0) {
                console.log("reloading...")
                window.location.reload()
            }

            //隐藏本组件
            parent.css("display", "none");

            //获取密码
            var password = JSON.parse(Base64.decode($.cookie("user"))).password;
            //睁眼闭眼图片
            var close_eye_svg = '<svg t="1676457166299" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3033" width="32" height="32"><path d="M930.024 339.358c8.607-12.84 5.644-29.914-5.644-39.933-12.84-10.018-29.915-7.196-39.933 5.644-1.411 1.411-159.731 188.235-347.965 188.235-182.59 0-347.966-188.235-349.377-189.646-10.018-11.43-28.503-12.84-39.932-2.822-11.43 10.019-12.84 28.503-2.822 39.933 2.822 4.233 37.11 42.755 91.295 85.51l-72.81 75.632c-11.43 11.43-10.02 29.914 1.41 39.933 2.822 5.644 10.019 8.607 17.074 8.607 7.196 0 14.252-2.822 20.037-8.607l78.454-81.277c37.111 25.681 81.277 49.951 129.817 67.025l-29.914 101.314c-4.233 15.662 4.233 31.325 20.037 35.7h8.607c12.84 0 24.27-8.608 27.092-21.449l29.915-101.313c22.859 4.233 47.129 7.196 71.258 7.196 24.27 0 48.54-2.822 71.258-7.196l29.914 99.902c2.822 12.84 15.663 21.448 27.092 21.448 2.823 0 5.645 0 7.197-1.41 15.662-4.234 24.27-20.038 20.037-35.7l-30.338-99.903c48.54-17.074 92.706-41.344 129.817-67.025l77.043 79.866c5.644 5.644 12.84 8.607 20.037 8.607s14.252-2.822 20.037-8.607c11.43-11.43 11.43-28.504 1.411-39.933l-72.669-75.632c58.276-42.755 92.565-84.1 92.565-84.1z m0 0" p-id="3034" fill="#1296db"></path></svg>'
            var open_eye_svg = '<svg t="1676459405312" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3792" width="32" height="32"><path d="M924.1 446.3c-75.7-68.5-229.7-183.5-411-183.5-181.5 0-335.6 115.2-411.3 183.8-18 16.3-28.4 39.6-28.4 63.8 0 24.2 10.3 47.5 28.4 63.8C177.5 642.8 331.7 758 513.1 758c181.3 0 335.3-115 411-183.5 18.1-16.4 28.5-39.8 28.5-64.1 0-24.3-10.4-47.7-28.5-64.1z m-44.3 79.3C811.2 587.8 672.3 692 513.1 692c-159.3 0-298.3-104.4-367-166.7-5.8-5.3-6.7-11.6-6.7-14.9 0-3.3 0.9-9.7 6.7-14.9 68.7-62.3 207.6-166.7 367-166.7 159.1 0 298 104.3 366.7 166.4 5.9 5.3 6.8 11.8 6.8 15.2s-0.9 9.9-6.8 15.2z" fill="#1296db" p-id="3793"></path><path d="M513 378.4c-72.8 0-132.1 59.2-132.1 132.1s59.3 132 132.1 132 132.1-59.2 132.1-132.1-59.2-132-132.1-132z m0 198.1c-36.4 0-66-29.6-66-66s29.6-66 66-66 66 29.6 66 66-29.6 66-66 66z" fill="#1296db" p-id="3794"></path></svg>'
            //先隐藏密码
            password_input.attr("type", "password");
            password_input.val(password);
            //在 password-input 下方添加密码开关
            var switch_button = createButton("show", "switch_button", password_input, function(){
                if (password_input.attr("type") == "password") {
                    password_input.attr("type", "text");
                    $(switch_button).html(open_eye_svg);
                } else {
                    password_input.attr("type", "password");
                    $(switch_button).html(close_eye_svg);
                }
            })
            
        </script>
    </body>
    """
    # 执行脚本
    st.components.v1.html(html=code, height=0)


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


def showUser():
    # 6.从应用会话中检测坚果云客户端类
    # 7.如果没有类
    if st.session_state.get("jgy") is None:
        with st.spinner("正在尝试连接坚果云盘..."):
            # 8.实例化坚果云客户端类
            jgy = JianGuoYunClient(username=username, password=password)
            # 9.执行登录
            login_jgy = jgy.login()
    # 7.如果已有该类
    else:
        # 8.直接从应用会话中获取此类实例
        jgy = st.session_state.jgy
        # 9.伪代码模拟登录成功
        login_jgy = {"status": 200}
    # 10.若登录成功
    if login_jgy["status"] == 200:
        # 11.保存用户配置于应用会话
        st.session_state.user = user
        # 12.保存坚果云客户端类实例于应用会话
        st.session_state.jgy = jgy
        # 13.展示已登录的坚果云账户
        st.success("已成功连接至坚果云盘！")
        st.text_input(label="[坚果云]账户：", key="show_username", disabled=True, value=username)
        st.text_input(label="[坚果云]应用密码：", key="show_password", disabled=True)
        addActionButton(action_id="jgy-action", action_text="【云√】", action_color="green", action_href="./首页")
        # 14.以 cookie 形式保存用户配置
        JSCookieManager(key="user", value=json.dumps(user))
        # 15.插入 js 控制密码密/明文切换
        insertPasswordJS()
        # 16.提供登出选项
        if st.button("断开连接"):
            with st.spinner("正在断开连接..."):
                # 17.断开连接
                disconnect()
                # 18.刷新页面
                refreshPage()
        showActionInfo()
    # 10.若登录失败
    else:
        # 11.提示登录失败
        st.error(f"连接坚果云盘失败：{login_jgy['error']}")
        # 12.断开连接
        disconnect()
        # 13.如果是自动登录的, 就刷新页面
        if auto_input:
            refreshPage()


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

# ** 判断是否是自动登录 ** #
auto_input = False
# 1.首先实例化双向的 cookie 管理器
cm = CookieManager()
# 2.然后从本地 cookie 中获取用户配置
user = cm.get("user")
# 3.若获取成功
if user and user.get("code") == 200:
    auto_input = True
    # 4.提取坚果云账户配置
    user = json.loads(base64.b64decode(user["value"]).decode())
    username = user["username"]
    password = user["password"]
    # 5.进行后续操作
    showUser()
# 3.若获取失败
else:
    # 4.提示输入坚果云账户配置
    username = st.text_input(label="输入账号：", key="username")
    password = st.text_input(label="输入应用密码：", key="password")
    confirm = st.button("确定")
    if confirm:
        user = {
            "username": username,
            "password": password,
        }
        # 5.执行后续操作
        showUser()