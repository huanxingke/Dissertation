import base64
import json

import streamlit as st


def chemicalsCard(chemicals):
    code = """
    <html>
        <head>
            <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1, maximum-scale=1, user-scalable=no"/>
            <script type="text/javascript" src="https://cdn.staticfile.org/jquery/3.6.3/jquery.min.js"></script>
            <link rel="stylesheet" href="https://weui.shanliwawa.top/weui/css/weui.css" type="text/css"/>
            <link rel="stylesheet" href="https://weui.shanliwawa.top/weui/css/weuix.css" type="text/css"/>
            <script type="text/javascript" src="https://weui.shanliwawa.top/weui/js/zepto.min.js"></script>
            <script type="text/javascript" src="https://weui.shanliwawa.top/weui/js/zepto.weui.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        </head>
        <body>
            <div id="chemicals"></div>
            <script type="text/javascript">
                var chemicals = JSON.parse(Base64.decode(`%s`));
                $("#chemicals").text(chemicals[0]["cas_number"]);
            </script>
        </body>
    </html>
    """ % base64.b64encode(json.dumps(chemicals).encode()).decode()
    st.components.v1.html(html=code)