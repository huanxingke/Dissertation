import streamlit as st


def pageStyle():
    # 嵌入 js 脚本
    code = """
    <head>
        <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
        <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
    </head>
    <body>
        <script>
            //注销: 清除所有 cookie
            function clearAllCookie() {
                try {
                    var user = $.cookie("user");
                    var userinfo = $.cookie("userinfo");
                    var chemical_favorites = $.cookie("chemical_favorites");
                    var chemicals_query_items = $.cookie("chemicals_query_items");
                    var learning_cookie = $.cookie("learning_cookie");
                    if (user == undefined && userinfo == undefined && learning_cookie == undefined) {
                        if (chemical_favorites == undefined && chemicals_query_items == undefined) {
                            return alert("无需注销！");
                        }
                    }
                    if (confirm("确定注销吗？这将清除所有本地cookie并断开坚果云连接！") == true){ 
                        $.removeCookie("user", { path: "/"});
                        $.removeCookie("userinfo", { path: "/"});
                        $.removeCookie("chemical_favorites", { path: "/"});
                        $.removeCookie("query_chemicals", { path: "/"});
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
                
            //判断是电脑端还是手机端
            function isMobile() {
                var userAgentInfo = navigator.userAgent;
                var mobileAgents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
                var mobile_flag = false;
                //根据userAgent判断是否是手机
                for (var v = 0; v < mobileAgents.length; v++) {
                   if (userAgentInfo.indexOf(mobileAgents[v]) > 0) {
                         mobile_flag = true;
                         break;
                   }
                }
                return mobile_flag;
            }
            
            //主菜单增加几个按钮
            function addActionButton(color, id, text, href="javascript:void(0);", func="") {
                if (root_document.find("#" + id).length > 0) {
                    return
                }
                var action_a = window.top.document.createElement("a");
                $(action_a).css("color", color);
                $(action_a).css("text-decoration", "none");
                $(action_a).attr("id", id);
                $(action_a).attr("href", href);
                $(action_a).text(text)
                if (func != "") {
                    $(action_a).click(function(){func()});
                }
                MainMenu.before(action_a);
            }
            
            //获取根文档
            var root_document = $(window.frameElement).parents().find("#root");
            //隐藏该组件
            $(window.frameElement).parent().hide();
            //该组件后续的div全显示
            $(window.frameElement).parent().nextAll().show();
            //class="stHidden"的div隐藏
            //root_document.find(".stHidden").parent().hide();
            
            //进度条功能区删除
            var progress_box = $(window.frameElement).parents().find("#root").find("#progress-box");
            if (progress_box.length > 0) {
                progress_box.remove();
            }
            
            //(1)修改底部说明为华工
            var footer = root_document.find("footer");
            footer.html("<p style='height:20px;line-height:20px;font-size=20px'><img src='https://www.scut.edu.cn/_upload/article/images/93/f1/da8bef494e929b2303b75fcae24a/76c44c1f-cc13-4b1c-b69c-1cb9e8e8aa3a.png' style='border-radius:50%;height:20px'/>&nbsp;South China University of Technology</p>")
            
            //(2)修改页面边距, 只更改电脑端的
            if (isMobile() == false) {
                //然后边距调整
                footer.css("padding", "10px 0 10px 50px")
                //主页面边框减小
                root_document.find("section[tabindex=0]").find("div[class*='block-container']").css("padding", "50px");
                //侧边栏上边间隔减少
                root_document.find("div[data-testid='stSidebarNav']").find("ul").css("padding", "50px 0 16px 0"); 
            }
            
            //(3)页面顶部菜单增加几个按钮
            //获取主菜单
            var MainMenu = root_document.find("#MainMenu");
            //名字
            addActionButton("blue", "userinfo-action", "游客", href="./个人信息", func="");
            //坚果云连接状态
            addActionButton("orange", "jgy-action", "[云×]", href="./首页", func="");
            //注销按钮
            addActionButton("red", "exit-action", "[注销]", href="javascript:void(0);", func=clearAllCookie);
        </script>
    </body>
    """
    # 执行脚本
    st.components.v1.html(html=code, height=0)