import streamlit as st


def footer():
    # 嵌入 js 脚本
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
    </head>
    <body>
        <script>
            //获取根文档
            var root_document = $(window.frameElement).parents("#root");
            //隐藏该组件
            $(window.frameElement).parent().hide();
            //该组件后续的div全显示
            $(window.frameElement).parent().nextAll().show();
            //class="stHidden"的div隐藏
            root_document.find(".stHidden").parent().hide();
            //获取底部说明
            var footer = root_document.find("footer");
            footer.html("<p style='height:20px;line-height:20px;font-size=20px'><img src='https://www.scut.edu.cn/_upload/article/images/93/f1/da8bef494e929b2303b75fcae24a/76c44c1f-cc13-4b1c-b69c-1cb9e8e8aa3a.png' style='border-radius:50%;height:20px'/>&nbsp;South China University of Technology</p>")

        </script>
    </body>
    """
    # 执行脚本
    st.components.v1.html(html=code, height=0)