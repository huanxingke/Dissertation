import time

import streamlit as st


def refreshPage(alert="null"):
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
    </head>
    <body>
        <script>
            //获取根文档
            var root_document = $(window.top.document);
            //隐藏该组件
            $(window.frameElement).parent().hide();
            //该组件后续的div全显示
            $(window.frameElement).parent().nextAll().show();
            //class="stHidden"的div隐藏
            root_document.find(".stHidden").parent().hide();
            if ("%s" != "null") {
                alert("%s");
            };
            //刷新整个页面
            window.top.location.reload()
        </script>
    </body>""" % (alert, alert)
    if not alert:
        with st.spinner("即将刷新页面..."):
            waits = 0
            for i in range(2):
                time.sleep(1)
                waits += 1
            if waits >= 2:
                st.components.v1.html(html=code, height=0)
    else:
        st.components.v1.html(html=code, height=0)