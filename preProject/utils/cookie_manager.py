import re

import streamlit as st


def CookieManager(key, value="", delete=False, expires=365, senseless=True):
    isStr = lambda x: False if (not isinstance(x, str)) or (not "".join([re.sub(r"\s+", "", i) for i in x])) else True
    # 键只能为非空字符串
    if isStr(key):
        # 键前后不能留有空白字符
        key = key.strip()
        if not delete:
            # 设置应用会话
            if not st.session_state.get("cookie"):
                st.session_state.cookie = {}
            st.session_state.cookie[key] = value
            # 储存 cookie
            code = """
            <head>
                <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
                <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
            </head>
            <body>
                <script>
                    //隐藏本组件
                    var parent = $(window.frameElement).parent();
                    parent.css("display", "none");
                    //设置 cookie
                    try {
                        $.cookie(`%s`, `%s`, { expires: %s, path: "/" });
                    } catch(err) {
                        console.log(err)
                    }
                </script>
            </body>
            """ % (key, value, expires)
        else:
            # 从应用会话中删除
            if st.session_state.get("cookie") and key in st.session_state.cookie:
                del st.session_state.cookie[key]
            # 删除 cookie
            code = """
            <head>
                <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
                <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
            </head>
            <body>
                <script>
                    //隐藏本组件
                    var parent = $(window.frameElement).parent();
                    parent.css("display", "none");
                    //删除 cookie
                    try {
                        $.removeCookie(`%s`, { path: "/" });
                    } catch(err) {
                        console.log(err)
                    }
                </script>
            </body>
            """ % key
        st.components.v1.html(html=code, height=0)
    elif not senseless:
        # 提示键只能为非空字符串
        code = """
        <head>
            <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
        </head>
        <body>
            <script>
                //隐藏本组件
                var parent = $(window.frameElement).parent();
                parent.css("display", "none");
                alert("Cookie键只能为非空字符串！")
            </script>
        </body>"""
        st.components.v1.html(html=code, height=0)


# key_input = st.text_input("输入键：", key="key_input")
# value_storage = st.text_input("输入值：", key="value_storage")
# if st.button("添加"):
#     CookieManager(key_input, value_storage, senseless=False)
# if st.button("删除"):
#     CookieManager(key_input, delete=True, senseless=False)
# st.write(st.session_state.get("cookie"))