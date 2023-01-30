import base64
import json

import streamlit as st


# 一些说明性文字
st.button("★本页说明：", disabled=True)
st.markdown("""
- 由于\
（1）Streamlit暂无原生的持久化储存api；\
（2）双向组件与页面间的异步通讯会导致千奇百怪的错误；\
（3）课题要求不能使用自己部署的服务器；\
因此暂时先使用「半自动化管理cookie」的方式来存储和读取数据。\n
- 您可以在包括但不限于\
（1）读取您所设置的用户信息；\
（2）读取您的学习与考试记录；\
（3）考试时闪退恢复进度；\
等情况打开本页面，重新手动加载cookie并将其更新至应用会话中。
""")
st.info("注：（1）本程序存储和读取的数据完全基于您的本地计算机，不提供任何的云服务！\
（2）某些浏览器不支持cookie插件，开启隐私模式也可能导致无法使用！")

# 显示 cookie_string
st.text_area(
    # 请勿修改 [Chemical-Cookie]
    label="[Chemical-Cookie]请将以下字符复制于输入框中:",
    key="cookie-string", disabled=True,
    value="这里将存放base64加密的cookie字符串..."
)
# cookie_string输入框
cookie_input = st.text_area(
    # 请勿修改 [Cookie-Input]
    label="[Cookie-Input]请将复制的字符粘贴至下方:",
    placeholder="请复制cookie字符串于此以更新会话状态！",
    key="Cookie-Input"
)
# 嵌入 js 脚本
code = """
<head>
    <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
    <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
</head>
<body>
    <script>
        //复制文本
        function copy(text) {
            var copy_element = window.top.document.createElement("input");
            copy_element.setAttribute("value", text);
            window.top.document.body.appendChild(copy_element);
            copy_element.select();
            if (window.top.document.execCommand("copy")) {
                window.top.document.execCommand("copy");
                window.top.document.body.removeChild(copy_element);
                alert("复制成功！")
            } else {
                window.top.document.body.removeChild(copy_element);
                alert("复制失败！请手动复制！")
            }
        }
        
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
            $(new_button).css("color", "white");
            $(new_button).text(label);
            //绑定事件
            $(new_button).click(function(){
                //保证页面显示的cookie_string最新
                cookie_string = Base64.encode(JSON.stringify($.cookie()));
                textarea_space.val(cookie_string);
                textarea_space.attr("value", cookie_string);
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
        //获取textarea元素
        var textarea_div = root_document.find("label:contains(Chemical-Cookie)").parent().parent();
        var textarea_space = textarea_div.find("textarea");
        var input_textarea_div = root_document.find("label:contains(Cookie-Input)").parent().parent();
        var input_textarea_space = input_textarea_div.find("textarea");
        
        //判断以上获取的元素是否存在, 不存在则刷新一下页面
        if (css_button.length == 0 || textarea_space.length == 0 || input_textarea_space.length == 0) {
            console.log("reloading...")
            window.location.reload()
        }
        
        //隐藏本组件
        parent.css("display", "none");
        //获取streamlit按钮样式
        css_button.css("color", "white");
        var button_css_style = css_button.attr("class");
        //加载并显示cookie字符串
        var cookie_string = Base64.encode(JSON.stringify($.cookie()));
        textarea_space.val(cookie_string);
        textarea_space.attr("value", cookie_string);
        //在textarea下方创建复制按钮
        var copy_button = createButton("复制", "copy_button", textarea_space, function(){
            //保证cookie_string最新
            cookie_string = Base64.encode(JSON.stringify($.cookie()));
            //复制
            copy(cookie_string);
        })
        //input_textarea下方设置一个确定按钮
        var confirm_button = createButton("确定", "confirm_button", input_textarea_space, function(){
            alert("已尝试设置会话！")
        })
    </script>
</body>
"""
# 执行脚本
st.components.v1.html(html=code, height=0)
# 解密 cookie_string 并加入会话状态
if cookie_input:
    try:
        cookie_input = json.loads(base64.b64decode(cookie_input).decode())
        st.session_state.cookie = cookie_input
        st.success("cookie解密成功！已读取会话！")
    except:
        st.error("cookie字符串解密出错！请检查是否粘贴错误！")
if not st.session_state.get("cookie"):
    st.write("◆ 已设置会话状态：无")
else:
    st.write(" ◆ 已设置会话状态：")
    st.write(st.session_state.get("cookie"))