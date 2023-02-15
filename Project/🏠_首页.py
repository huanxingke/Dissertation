import base64
import json

import streamlit as st

from components.CookieManager import CookieManager, JSCookieManager, refreshPage
from components.Webdav import JianGuoYunClient

cm = CookieManager()


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
                var new_button = window.top.document.createElement("button");
                $(new_button).attr("kind", "primary");
                $(new_button).attr("class", button_css_style);
                $(new_button).attr("id", id);
                $(new_button).text(label);
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
            //先隐藏密码
            password_input.attr("type", "password");
            password_input.val(password);
            //在 password-input 下方添加密码开关
            var switch_button = createButton("show", "switch_button", password_input, function(){
                if (password_input.attr("type") == "password") {
                    password_input.attr("type", "text");
                    $(switch_button).text("hide")
                } else {
                    password_input.attr("type", "password");
                    $(switch_button).text("show")
                }
            })
        </script>
    </body>
    """
    # 执行脚本
    st.components.v1.html(html=code, height=0)


def showUser():
    if st.session_state.get("jgy") is None:
        jgy = JianGuoYunClient(username=username, password=password)
        login_jgy = jgy.login()
    else:
        jgy = st.session_state.jgy
        login_jgy = {"status": 200}
    if login_jgy["status"] == 200:
        st.session_state.user = user
        st.session_state.jgy = jgy
        st.success("已成功连接至坚果云盘！")
        st.text_input(label="[坚果云]账户：", key="show_username", disabled=True, value=username)
        st.text_input(label="[坚果云]应用密码：", key="show_password", disabled=True)
        JSCookieManager(key="user", value=json.dumps(user))
        insertPasswordJS()
        if st.button("断开连接"):
            del st.session_state.jgy
            del st.session_state.user
            JSCookieManager(key="user", delete=True)
            refreshPage()
    else:
        st.error(f"连接坚果云盘失败：{login_jgy['error']}")


user = cm.get("user")
if user and user.get("code") == 200:
    user = json.loads(base64.b64decode(user["value"]).decode())
    username = user["username"]
    password = user["password"]
    showUser()
else:
    username = st.text_input(label="输入账号：", key="username")
    password = st.text_input(label="输入应用密码：", key="password")
    if st.button("确定"):
        user = {
            "username": username,
            "password": password,
        }
        showUser()