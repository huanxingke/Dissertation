import base64
import json

import streamlit as st


def chemicalsCard(chemical):
    code = """
    <html>
        <head>
            <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1, maximum-scale=1, user-scalable=no"/>
            <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
            <link rel="stylesheet" href="https://weui.shanliwawa.top/weui/css/weui.css" type="text/css"/>
            <link rel="stylesheet" href="https://weui.shanliwawa.top/weui/css/weuix.css" type="text/css"/>
            <script type="text/javascript" src="https://weui.shanliwawa.top/weui/js/zepto.min.js"></script>
            <script type="text/javascript" src="https://weui.shanliwawa.top/weui/js/zepto.weui.js"></script>
            <script type="text/javascript" src="https://unpkg.com/art-template@4.13.2/lib/template-web.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/js-base64@3.7.4/base64.min.js"></script>
            <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
            <style>
                .box {
                    width: 100%%px;
                    height: 524px;
                    display: grid;
                    justify-content: left;
                    align-items: center;
                }
                .card {
                    padding: 10px 10px 10px 10px;
                    border-radius: 20px;
                    width: 300px;
                    height: 500px;
                    display: grid;
                    grid-template-rows: repeat(10, 50px);
                }
                .card-header {
                    grid-row-start: 1;
                    grid-row-end: 4;
                    display: grid;
                    grid-template-columns: 120px 180px;
                    grid-template-rows: repeat(6, 25px);
                }
                .chemical-name-div {
                    grid-column-start: 1;
                    grid-column-end: 2;
                    grid-row-start: 1;
                    grid-row-end: 5;
                    display: grid;
                    justify-content: center;
                    align-items: center;
                }
                .chemical-name {
                    font-size: 18px;
                    line-height: 25px;
                    font-weight: bold;
                    word-break: break-all;
                    text-overflow: ellipsis;
                    overflow: hidden;
                    display: -webkit-box;
                    -webkit-box-orient: vertical;
                    -webkit-line-clamp: 4;
                    cursor: pointer;
                    text-decoration: underline;
                }
                .cas-number-div {
                    grid-column-start: 1;
                    grid-column-end: 2;
                    grid-row-start: 5;
                    grid-row-end: 7;
                    display: grid;
                    justify-content: left;
                    align-items: top;
                }
                .cas-number {
                    font-size: 15px;
                    line-height: 25px;
                    word-break: break-all;
                    text-overflow: ellipsis;
                    overflow: hidden;
                    display: -webkit-box;
                    -webkit-box-orient: vertical;
                    -webkit-line-clamp: 2;
                }
                .struct-div {
                    grid-column-start: 2;
                    grid-column-end: 3;
                    grid-row-start: 1;
                    grid-row-end: 9;
                    display: grid;
                    justify-content: center;
                    align-items: center;
                }
                .struct {
                    margin: 5px;
                    border-radius: 5px;
                    width: 168px;
                    height: 138px;
                    cursor: pointer;
                    display: grid;
                    justify-content: center;
                    align-items: center;
                }
                .struct-img {
                    width: 100%%;
                    height: 100%%;
                    border-radius: 5px;
                    object-fit: contain;
                    z-index: -1;
                }
                .struct-img-alt {
                    height: 20px;
                    line-height: 20px;
                    font-size: 20px;
                }
                .category {
                    position: absolute;
                    border-radius: 5px 0px 5px 0px;
                    top: 18px;
                    left: 138px;
                    z-index: 1;
                    font-size: 12px;
                    line-height: 15px;
                    word-break: break-all;
                    max-width: 160px;
                }
                .ghs-div {
                    grid-row-start: 4;
                    grid-row-end: 5;
                    display: grid;
                    grid-template-columns: repeat(auto-fit);
                }
                .ghs {
                    cursor: pointer;
                    margin: 5px;
                    height: 40px;
                    display: grid;
                    justify-content: center;
                    align-items: center;
                }
                .ghs-img {
                    height: 40px;
                }
                .decoration-div {
                    grid-column-start: 1;
                    grid-column-end: 3;
                    display: grid;
                    justify-content: left;
                    align-items: top;
                }
                .decoration {
                    font-size: 15px;
                    line-height: 25px;
                    word-break: break-all;
                    text-overflow: ellipsis;
                    overflow: hidden;
                    display: -webkit-box;
                    -webkit-box-orient: vertical;
                    -webkit-line-clamp: 2;
                }
                .info-label {
                    cursor: pointer;
                    color: #00BFFF;
                    text-decoration: underline;
                }
                .hideDom {
                    display: none;
                }
                .favorite {
                    position: absolute;
                    border-radius: 50%%;
                    top: 0px;
                    left: 0px;
                    width: 25px;
                    height: 25px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="box" id="chemical"></div>
            <script type="text/html" id="chemical-template">
                <div class="card" style="border:2px inset {{color}}">
                    <div class="favorite" onclick="switchFavorite(this)">
                        <svg t="1678024998895" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4869" width="25" height="25"><path d="M519.2 807.2l255.2 133.6c12 6.4 25.6-4 23.2-16.8L748.8 640c-0.8-4.8 0.8-10.4 4.8-14.4L960 424.8c9.6-9.6 4-25.6-8.8-27.2l-284.8-41.6c-5.6-0.8-9.6-4-12-8.8l-128-257.6c-5.6-12-23.2-12-28.8 0L370.4 348c-2.4 4.8-7.2 8-12 8.8L73.6 398.4c-13.6 1.6-18.4 17.6-8.8 27.2l206.4 200.8c4 4 5.6 8.8 4.8 14.4l-48.8 284c-2.4 12.8 11.2 23.2 23.2 16.8L505.6 808c4-3.2 8.8-3.2 13.6-0.8z" p-id="4870" fill="#bfbfbf"></path></svg>
                    </div>
                    <div class="card-header">
                        <div class="chemical-name-div">
                            <p class="chemical-name" onclick="showNames({{name}}, {{enName}})">{{name[0]}}</p>
                        </div>
                        <div class="cas-number-div">
                            <p class="cas-number"><span class="info-label">CAS</span>：<span id="cas-number">{{cas_number[0]}}</span></p>
                        </div>
                        <div class="struct-div">
                            {{if struct_pic[0] != ""}}
                                <div id="have-struct_pic" class="struct" style="border:1px dashed {{color}}" onclick="showPic(this)">
                                    <p class="f-white category" style="background:{{color}};">{{category}}</p>
                                    <img class="struct-img" src="{{struct_pic[0]}}"/>
                                </div>
                                <div id="no-struct_pic" class="struct hideDom" style="border:1px dashed {{color}}">
                                    <label class="label f-white bg-green category" style="background:{{color}}">{{category}}</label>
                                    <p class="struct-img-alt">无结构式图片</p>
                                </div>
                            {{else}}
                                <div id="have-struct_pic" class="struct hideDom" style="border:1px dashed {{color}}" onclick="showPic(this)">
                                    <label class="label f-white bg-green category" style="background:{{color}}">{{category}}</label>
                                    <img class="struct-img" src="{{struct_pic[0]}}"/>
                                </div>
                                <div id="no-struct_pic" class="struct" style="border:1px dashed {{color}}">
                                    <label class="label f-white bg-green category" style="background:{{color}}">{{category}}</label>
                                    <p class="struct-img-alt">无结构式图片</p>
                                </div>
                            {{/if}}
                        </div>
                    </div>
                    <div class="ghs-div">
                        {{each ghs_pic as ghs_pic_src ghs_pic_index}}
                            <div class="ghs" style="grid-column-start:{{ghs_pic_index+1}};grid-column-end:{{ghs_pic_index+2}};">
                                {{if ghs_pic_src}}
                                    <img class="ghs-img" src="{{ghs_pic_src}}" onclick="showGHSMeanings('{{ghs_pic_index}}')"/>
                                {{else}}
                                    GHS-?
                                {{/if}}
                            </div>
                        {{/each}}
                    </div>
                    <div class="decoration-div" style="grid-row-start:5;grid-row-end:6;">
                        <p class="decoration">
                            <span class="info-label" style="font-weight:bold" onclick="showText('{{name[0]}}', this)">
                                环境危害
                            </span>：
                            <span>{{huanjingweihai}}{{if critical_quantity}}临界量：{{critical_quantity}}t{{/if}}</span>
                        </p>
                    </div>
                    <div class="decoration-div" style="grid-row-start:6;grid-row-end:7;">
                        <p class="decoration">
                            <span class="info-label" style="font-weight:bold" onclick="showText('{{name[0]}}', this)">
                                活性反应
                            </span>：
                            <span>{{ranshaoyubaozhaweixianxing + huoxingfanying}}</span>
                        </p>
                    </div>
                    <div class="decoration-div" style="grid-row-start:7;grid-row-end:8;">
                        <p class="decoration">
                            <span class="info-label" style="font-weight:bold" onclick="showText('{{name[0]}}', this)">
                                毒性
                            </span>：
                            <span>{{zhongdubiaoxian}}</span>
                        </p>
                    </div>
                    <div class="decoration-div" style="grid-row-start:8;grid-row-end:9;">
                        <p class="decoration">
                            <span class="info-label" style="font-weight:bold" onclick="showText('{{name[0]}}', this)">
                                急救措施
                            </span>：
                            <span>{{jijiucuoshi}}</span>
                        </p>
                    </div>
                    <div class="decoration-div" style="grid-row-start:9;grid-row-end:10;">
                        <p class="decoration">
                            <span class="info-label" style="font-weight:bold" onclick="showText('{{name[0]}}', this)">
                                灭火方法
                            </span>：
                            <span>{{miehuofangfa}}</span>
                        </p>
                    </div>
                    <div class="decoration-div" style="grid-row-start:10;grid-row-end:11;">
                        <p class="decoration">
                            <span class="info-label" style="font-weight:bold" onclick="showText('{{name[0]}}', this)">
                                泄露处置
                            </span>：
                            <span>{{xielouyingjichuzhi}}</span>
                        </p>
                    </div>
                </div>
            </script>
            <script type="text/javascript">
                function showPic(obj) {
                    let gall = gallery($(obj).find("img").attr("src"));
                    //相册关闭按钮
                    var close_botton = $("button.weui-hidden_abs.weui-gallery__close");
                    //底部删除区域更换为相册关闭按钮
                    $("a.weui-gallery__del").remove();
                    $("div.weui-gallery__opr").html(
                        '<button class="weui-btn weui-btn_mini  bg-orange weui-gallery__close">关闭预览</button>'
                    );
                    //删除原来的关闭按钮
                    close_botton.remove();
                    //点击任意区域关闭相册
                    $("div.weui-gallery.weui-animate-fade-in").click(function(){gall.hide(function(){})});
                    //相册外部区域的颜色
                    let media = window.top.matchMedia("(prefers-color-scheme:dark)");
                    let prefersDarkMode = media.matches;
                    if (prefersDarkMode) {
                         $("div.weui-gallery__opr").attr("style", "display:block;opacity:1;background:black");
                         $("div.weui-gallery.weui-animate-fade-in").attr("style", "display:block;opacity:1;background:black");
                    } else {
                         $("div.weui-gallery__opr").attr("style", "display:block;opacity:1;background:white")
                         $("div.weui-gallery.weui-animate-fade-in").attr("style", "display:block;opacity:1;background:white")
                    }
                }

                function switchDarkMode() {
                    let media = window.top.matchMedia("(prefers-color-scheme:dark)");
                    let prefersDarkMode = media.matches;
                    if (prefersDarkMode) {
                        //深色模式
                        $("body").attr("style", "color:white");
                        $(".struct-img").attr("style", "background:white");
                    } else {
                        //亮色模式
                        $("body").attr("style", "color:black");
                        $(".struct-img").attr("style", "background:white");
                    }
                }

                function modPrompts() {
                    $(".weui-dialog__btn.primary").text("复制")
                    $("#weui-prompt-input").attr("disabled", "disabled");
                    $("#weui-prompt-input").attr("style", "color:black;white-space:pre-line");
                    $(".weui-prompt-text").attr("style", "color:black");
                }

                function copy() {
                    var input = window.top.document.createElement("input");
                    window.top.document.body.appendChild(input);
                    input.setAttribute("value", $("#weui-prompt-input").val());
                    input.select();
                    if (window.top.document.execCommand("copy")) {
                        window.top.document.execCommand("copy");
                        $.toast("复制成功");
                    } else {
                        $.toast("复制失败", "cancel");
                    }
                    window.top.document.body.removeChild(input);
                }

                function showNames(name, enName) {
                    $.prompts({
                        title: name[0],
                        text: "名称",
                        input: "中文名：" + name.join("；") + "\\n\\n英文名：" + enName.join("；"),
                        empty: false,
                        onOK: function (v) {copy()},
                        onCancel: function () {}
                    });
                    modPrompts();
                }

                function showGHSMeanings(ghs_pic_index) {
                    var title = chemical["xiangxingtu"][parseInt(ghs_pic_index)];
                    var meaning = chemical["ghs_meanings"][parseInt(ghs_pic_index)];
                    $.prompts({
                        title: title,
                        text: "象形图含义",
                        input: meaning,
                        empty: false,
                        onOK: function (v) {copy()},
                        onCancel: function () {}
                    });
                    modPrompts();
                }

                function showText(name, obj) {
                    $.prompts({
                        title: name,
                        text: $(obj).text(),
                        input: $(obj).next().text(),
                        empty: false,
                        onOK: function (v) {copy()},
                        onCancel: function () {}
                    });
                    modPrompts();
                }
                
                function switchFavorite(obj=null) {
                    var chemical_index = String(chemical.index);
                    var favorite_list = $.cookie("chemical_favorites");
                    if (favorite_list) {
                        favorite_list = favorite_list.split(",")
                    } else {
                        favorite_list = new Array();
                    }
                    var is_favorite = $.inArray(chemical_index, favorite_list);
                    var path = $(".favorite").find("svg").find("path");
                    if (obj != null) {
                        if (path.attr("fill") == "#bfbfbf") {
                            path.attr("fill", "#f4ea2a");
                            if (is_favorite == -1) {
                                favorite_list.push(chemical_index);
                                favorite_list = favorite_list.join(",");
                                var title = "已加入收藏";
                            }
                        } else {
                            path.attr("fill", "#bfbfbf");
                            if (is_favorite > -1) {
                                favorite_list.splice(is_favorite, 1);
                                favorite_list = favorite_list.join(",");
                                var title = "已取消收藏";
                            }
                        };
                        if ($.cookie("user")) {
                            console.log($.cookie("user"));
                            $.confirm("需要刷新页面才能同步收藏至云端，需要刷新吗？", title, function(){}, function(){window.top.location.reload()});
                        } else {
                            $.toast(title);
                        }
                        $.cookie("chemical_favorites", favorite_list);
                        $(".weui-dialog__btn.default").text("刷新");
                        $(".weui-dialog__btn.primary").text("稍后");
                    } else {
                        if (is_favorite == -1) {
                            path.attr("fill", "#bfbfbf");
                        } else {
                            path.attr("fill", "#f4ea2a");
                        }
                    }
                }
                
                //获取父节点
                var parent = $(window.frameElement).parent();
                //获取根文档
                parent.show();

                //渲染页面
                var chemical = JSON.parse(Base64.decode(`%s`));
                var html = template("chemical-template", chemical);
                $("#chemical").html(html);
                $(".cas-number > span").select({
                    title: "CAS号",
                    items: chemical["cas_number"],
                    onChange: function(d) {
                       $.each(chemical["cas_number"], function(cas_index, cas) {
                            if (cas == d.values) {
                                $("#cas-number").text(cas);
                                if (chemical["struct_pic"][cas_index]) {
                                    $(".struct-img").attr("src", chemical["struct_pic"][cas_index]);
                                    $("#no-struct_pic").removeClass("hideDom");
                                    $("#have-struct_pic").removeClass("hideDom");
                                    $("#no-struct_pic").addClass("hideDom");
                                } else {
                                    $("#no-struct_pic").removeClass("hideDom");
                                    $("#have-struct_pic").removeClass("hideDom");
                                    $("#have-struct_pic").addClass("hideDom");
                                }
                            }
                       })
                    },
                });
                switchFavorite();

                //深色模式和亮色模式切换
                //先切换为当前的模式
                switchDarkMode();
                //获取主页面媒体
                let media = window.top.matchMedia("(prefers-color-scheme:dark)");
                //监听模式切换
                let callback = e => {switchDarkMode()}
                if (typeof media.addEventListener === "function") {
                    media.addEventListener("change", callback);
                } else if (typeof media.addListener === "function" ) {
                    media.addListener(callback);
                }
            </script>
        </body>
    </html>
    """ % base64.b64encode(json.dumps(chemical).encode()).decode()
    st.components.v1.html(html=code, height=524)