import streamlit as st


def addActionButton(action_id, action_text, action_href="javascript:void(0);", action_color="blue", action_func=""):
    # 嵌入 js 脚本
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
    </head>
    <body>
        <script>
            function clearAllCookie() {
                try {
                    var user = $.cookie("user");
                    var userinfo = $.cookie("userinfo");
                    if (user == undefined && userinfo == undefined) {
                        return alert("无需注销！");
                    }
                    if (confirm("确定注销吗？这将清除所有本地cookie并断开坚果云连接！") == true){ 
                        $.removeCookie("user", { path: "/"});
                        $.removeCookie("userinfo", { path: "/"});
                        alert("已注销！");
                        window.top.location.reload();
                    } else{ 
                        alert("已取消注销操作！");
                    }
                } catch(err) {
                    alert("清除 cookie 失败！");
                    console.log(err);
                }
            };
        
            //获取父节点
            var parent = $(window.frameElement).parent();
            //获取根文档
            var root_document = $(window.frameElement).parents("#root");
            //主菜单
            var MainMenu = root_document.find("#MainMenu");
            if (root_document.find("#%s").length > 0) {
                var action_a = root_document.find("#%s");
                $(action_a).attr("style", "color:%s;text-decoration:none");
                $(action_a).attr("href", "%s");
                $(action_a).text("%s")
            } else {
                var action_a = window.top.document.createElement("a");
                $(action_a).attr("style", "color:%s;text-decoration:none");
                $(action_a).attr("id", "%s");
                $(action_a).attr("href", "%s");
                $(action_a).text("%s")
                $(action_a).click(function(){%s});
                MainMenu.before(action_a);
            }
            
            //底部
            $("footer").html("<p><i></i>South China University of Technology</p>")
    
            //隐藏本组件
            parent.css("display", "none");
        </script>
    </body>
    """ % (action_id, action_id, action_color, action_href, action_text, action_color, action_id, action_href, action_text, action_func)
    # 执行脚本
    st.components.v1.html(html=code, height=0)