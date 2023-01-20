import datetime
import re
import os

import streamlit.components.v1 as components
import streamlit as st


IS_RELEASE = True

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("cookie_manager", path=build_path)
else:
    _component_func = components.declare_component("cookie_manager", url="http://localhost:3000")


def Validation(func):
    def wrapper(self, *args, **kwargs):
        try:
            # Key must be str and not None.
            isStr = lambda x: False if (not isinstance(x, str)) or (not "".join([re.sub(r"\s+", "", i) for i in x])) else True
            # Make the key of component unique.
            self.components += 1
            if kwargs:
                if not isStr(kwargs.get("param")):
                    response = {"code": -1, "msg": "Key Not Allowed!"}
                else:
                    # Not start or end with \s+.
                    kwargs["param"] = kwargs["param"].strip()
                    response = func(self, *args, **kwargs)
            elif args:
                if not isStr(args[0]):
                    response = {"code": -1, "msg": "Key Not Allowed!"}
                else:
                    # Not start or end with \s+.
                    list_args = list(args)
                    list_args[0] = list_args[0].strip()
                    args = tuple(list_args)
                    response = func(self, *args)
            else:
                response = func(self)
            # Hide the component.
            hideComponent()
            return response
        except Exception as error:
            return {"code": -100, "msg": "Error!", "error": str(error)}

    return wrapper


class CookieManager(object):
    def __init__(self):
        self.cookie_manager = _component_func
        self.components = 0
        self.key = "CookieManagerComponent-%s"

    @Validation
    def get(self, param):
        response = self.cookie_manager(method="get", param=param, key=self.key % self.components)
        return response

    @Validation
    def set(self, param, value, timedelta=3600):
        # Expiration date.
        expires_at = datetime.datetime.now() + datetime.timedelta(days=timedelta)
        expires_at = expires_at.isoformat()
        response = self.cookie_manager(
            method="set", param=param, value=value,
            expires_at=expires_at, key=self.key % self.components
        )
        return response

    @Validation
    def delete(self, param):
        response = self.cookie_manager(method="del", param=param, key=self.key % self.components)
        return response

    @Validation
    def getAll(self):
        response = self.cookie_manager(method="all", key=self.key % self.components)
        return response


def hideComponent(component_name="cookie_manager"):
    st.components.v1.html(html="""
    <head>
        <script type="text/javascript" src="https://rawcdn.githack.com/huanxingke/Dissertation/7961470650c0f09bdfd720b4510d55f8141bc587/preProject/static/js/JQuery.js"></script>
    </head>
    <body>
        <script>
            var parent = $(window.frameElement).parent();
            parent.css("display", "none")
            var root_document = $(window.parent).parents("#root");
            var components = $(root_document).find("iframe[title*='%s']").parent();
            components.each(function(index, component) {
                $(component).css("display", "none")
            })
        </script>
    </body>
    """ % component_name, height=0)
