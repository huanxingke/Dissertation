import base64
import json

import streamlit as st


def chemicalsCard(chemical):
    code = """
    <html>
        <head>
            <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1, maximum-scale=1, user-scalable=no"/>
            <script type="text/javascript" src="https://cdn.staticfile.org/jquery/3.6.3/jquery.min.js"></script>
            <link rel="stylesheet" href="https://weui.shanliwawa.top/weui/css/weui.css" type="text/css"/>
            <link rel="stylesheet" href="https://weui.shanliwawa.top/weui/css/weuix.css" type="text/css"/>
            <script type="text/javascript" src="https://weui.shanliwawa.top/weui/js/zepto.min.js"></script>
            <script type="text/javascript" src="https://weui.shanliwawa.top/weui/js/zepto.weui.js"></script>
            <script type="text/javascript" src="https://unpkg.com/art-template@4.13.2/lib/template-web.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        </head>
        <body>
            <div id="chemicals" style="text-align:center"></div>
            <script type="text/html" id="chemicals-template">
                <h3>{{name[0]}}</h3>
                <div class="weui-flex">
                    {{each cas_number as cas_value cas_index}}
                        <div class="weui-flex__item">
                            <p>{{cas_value}}</p>
                            <p><img src="{{struct_pic[cas_index]}}" style="width:200px"/></p>
                        </div>
                    {{/each}}
                </div>
            </script>
            <script type="text/javascript">
                var chemicals = JSON.parse(Base64.decode(`%s`));
                var html = template("chemicals-template", chemicals[0]);
                $("#chemicals").html(html);
            </script>
        </body>
    </html>
    """ % base64.b64encode(json.dumps(chemical).encode()).decode()
    st.components.v1.html(html=code)