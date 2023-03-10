import streamlit as st


def addActionButton(action_id, action_text, action_href="javascript:void(0);", action_color="blue", action_func=""):
    # 嵌入 js 脚本
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
    </head>
    <body>
        <script>
            //获取根文档
            var root_document = $(window.frameElement).parents().find("#root");
            //隐藏该组件
            $(window.frameElement).parent().hide();
            //该组件后续的div全显示
            $(window.frameElement).parent().nextAll().show();
            //class="stHidden"的div隐藏
            //root_document.find(".stHidden").parent().hide();
            
            //主菜单
            var MainMenu = root_document.find("#MainMenu");
            if (root_document.find("#%s").length > 0) {
                var action_a = root_document.find("#%s");
                $(action_a).attr("style", "color:%s;text-decoration:none");
                $(action_a).attr("href", "%s");
                $(action_a).text("%s");
            } else {
                var action_a = window.top.document.createElement("a");
                $(action_a).attr("style", "color:%s;text-decoration:none");
                $(action_a).attr("id", "%s");
                $(action_a).attr("href", "%s");
                $(action_a).text("%s")
                $(action_a).click(function(){%s});
                MainMenu.before(action_a);
            }
        </script>
    </body>
    """ % (action_id, action_id, action_color, action_href, action_text, action_color,
           action_id, action_href, action_text, action_func)
    # 执行脚本
    st.components.v1.html(html=code, height=0)