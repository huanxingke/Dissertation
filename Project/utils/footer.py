import streamlit as st


def footer():
    # 嵌入 js 脚本
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
    </head>
    <body>
        <script>
            //获取父节点
            var parent = $(window.frameElement).parent();
            //获取根文档
            var root_document = $(window.frameElement).parents("#root");
            //获取底部说明
            var footer = root_document.find("footer");
            footer.html("<p><i></i>South China University of Technology</p>")
            //隐藏本组件
            parent.css("display", "none");
        </script>
    </body>
    """
    # 执行脚本
    st.components.v1.html(html=code, height=0)