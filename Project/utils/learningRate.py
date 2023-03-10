import time

import streamlit as st


def learningRate(chapter_index):
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
    </head>
    <body>
        <script>
            //隐藏该组件
            $(window.frameElement).parent().hide();
            //该组件后续的div全显示
            $(window.frameElement).parent().nextAll().show();
            //class="stHidden"的div隐藏
            $(window.frameElement).parents().find("#root").find(".stHidden").parent().hide();
            
            //章节
            var chapter = "%s";
            var learning_mode = "%s";
            var learning_cookie = $.cookie("learning_cookie");
            if (learning_cookie == undefined) {
                learning_cookie = {};
                learning_cookie[learning_mode] = {};
                learning_cookie[learning_mode][chapter] = 0;
            } else {
                learning_cookie = JSON.parse(Base64.decode(learning_cookie));
                if (learning_cookie[learning_mode] == undefined) {
                    learning_cookie[learning_mode] = {};
                }
                if (learning_cookie[learning_mode][chapter] == undefined) {
                    learning_cookie[learning_mode][chapter] = 0;
                }
            }
            console.log(learning_cookie);
            
            //进度条功能区
            var progress_box = $(window.frameElement).parents().find("#root").find("#progress-box");
            if (progress_box.length > 0) {
                progress_box.remove();
            }
            progress_div = '<div id="progress-box" style="display:grid;width:255px;height:42px;margin-top:20px;grid-template-rows:17px 5px 25px;"><div style="height:17px;display:flex;display:-webkit-flex;grid-row-start:1;grid-row-end:2;"><div style="width:202px;height:17px;border:1px solid #9e9e9e;border-radius:7.5px"><div style="width:0;height:15px;background:#325976;border-radius:7.5px" id="progress"></div></div><span style="margin-left:5px;width:48px;height:17px;line-height:17px;text-align:left" id="progress-text">0%%</span></div><div style="height:25px;display:flex;display:-webkit-flex;grid-row-start:3;grid-row-end:4;"><button id="clearLearningRate" style="height:25px;line-height:19px;border-radius:12.5px;width:90px;margin-left:0px;background:transparent;color:#9C9C9C">重置进度</button></div></div>'
            var sidebar_container = $(window.frameElement).parents().find("#root").find("section[data-testid='stSidebar']").find("div[data-testid='stVerticalBlock']");
            sidebar_container.after(progress_div);
            
            //初始化进度条
            var learning_rate = parseInt(learning_cookie[learning_mode][chapter]);
            var section = $(window.frameElement).parents().find("#root").find("section[tabindex=0]")[0];
            $(section).scrollTop(section.scrollHeight * learning_rate / 100 - section.clientHeight);
            $(window.frameElement).parents().find("#root").find("#progress").css("width", (2 * learning_rate).toString() + "px");
            if (learning_rate == 100) {
                $(window.frameElement).parents().find("#root").find("#progress-text").text("已完成");
            } else {
                $(window.frameElement).parents().find("#root").find("#progress-text").text(learning_rate + "%%");
            };
            //滚动条滚动事件
            $(section).scroll(function() {
                learning_rate_now = Math.round(100 * (this.scrollTop + this.clientHeight) / this.scrollHeight);
                if (learning_rate_now > learning_rate) {
                    learning_rate = learning_rate_now;
                    $(window.frameElement).parents().find("#root").find("#progress").css("width", (2 * learning_rate).toString() + "px");
                    if (learning_rate == 100) {
                        $(window.frameElement).parents().find("#root").find("#progress-text").text("已完成");
                    } else {
                        $(window.frameElement).parents().find("#root").find("#progress-text").text(learning_rate + "%%");
                    };
                    learning_cookie["timestamp"] = parseInt(new Date().getTime() / 1000);
                    learning_cookie[learning_mode][chapter] = learning_rate;
                    console.log(learning_cookie);
                    var cookie_string = Base64.encode(JSON.stringify(learning_cookie));
                    $.cookie("learning_cookie", cookie_string, { expires: 365, path: "/" });
                }
            });
            
            //按钮绑定事件
            $(window.frameElement).parents().find("#root").find("#clearLearningRate").click(function(){
                learning_rate = 0;
                $(section).scrollTop(0);
                learning_cookie["timestamp"] = parseInt(new Date().getTime() / 1000);
                learning_cookie[learning_mode][chapter] = learning_rate;
                console.log(learning_cookie);
                var cookie_string = Base64.encode(JSON.stringify(learning_cookie));
                $.cookie("learning_cookie", cookie_string, { expires: 365, path: "/" });
            });
        </script>
    </body>
    """
    learning_mode = st.session_state.get("learning_mode")
    if learning_mode == "Markdown":
        learning_mode = "M"
    else:
        learning_mode = "P"
    code %= (chapter_index, learning_mode[0])
    # 等待页面加载完成
    time.sleep(1)
    # 执行脚本
    st.components.v1.html(html=code, height=0)