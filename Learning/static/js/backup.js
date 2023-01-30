//于顶级页面加载js或css(未用到)
function loadJsOrCss(type, src) {
    var root_head = $(window.frameElement).parents("html").find("head");
    var first_script = root_head.find("script")[0];
    if (type == "js") {
        var append_js = window.top.document.createElement("script");
        append_js.type = "text/javascript";
        append_js.src = src;
        root_head[0].insertBefore(append_js, first_script);
    } else {
        var append_css = window.top.document.createElement("link");
        append_css.rel = "stylesheet";
        append_css.href = src;
        root_head[0].insertBefore(append_css, first_script);
    }
}

//复制文本
function copy(text) {
    var copy_element = window.top.document.createElement("input");
    copy_element.setAttribute("value", text);
    window.top.document.body.appendChild(copy_element);
    copy_element.select();
    if (window.top.document.execCommand("copy")) {
        window.top.document.execCommand("copy");
        window.top.document.body.removeChild(copy_element);
        alert("复制成功！")
    } else {
        window.top.document.body.removeChild(copy_element);
        alert("复制失败！请手动复制！")
    }
}

//生成txt并下载(未用到)
function download(filename, text) {
    var element = window.top.document.createElement("a");
    element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
    element.setAttribute("download", filename);
    element.style.display = "none";
    window.top.document.body.appendChild(element);
    element.click();
    window.top.document.body.removeChild(element);
}

//新建按钮
function createButton(label, id, beforeNode, func) {
    //防止重复创建
    if (root_document.find("#" + id).length > 0) {
        root_document.find("#" + id).remove();
    }
    //开始新建
    var new_button = window.top.document.createElement("button");
    $(new_button).attr("kind", "primary");
    $(new_button).attr("class", button_css_style);
    $(new_button).attr("id", id);
    $(new_button).css("color", "white");
    $(new_button).text(label);
    //绑定事件
    $(new_button).click(function(){
        //保证页面显示的cookie_string最新
        cookie_string = Base64.encode(JSON.stringify($.cookie()));
        textarea_space.val(cookie_string);
        textarea_space.attr("value", cookie_string);
        //执行函数
        func();
    });
    beforeNode.after(new_button);
    return new_button;
}

//隐藏本组件
var parent = $(window.frameElement).parent();
parent.css("display", "none");
//获取根文档
var root_document = $(window.frameElement).parents("#root");
//获取streamlit按钮
var css_button = root_document.find("div.row-widget.stButton").find("button");
//获取textarea元素
var textarea_div = root_document.find("label:contains(Chemical-Cookie)").parent().parent();
var textarea_space = textarea_div.find("textarea");
var input_textarea_div = root_document.find("label:contains(Cookie-Input)").parent().parent();
var input_textarea_space = input_textarea_div.find("textarea");

//判断以上获取的元素是否存在, 不存在则刷新一下页面
if (css_button.length == 0 || textarea_space.length == 0 || input_textarea_space.length == 0) {
    console.log("reloading...")
    window.location.reload()
}

//获取streamlit按钮样式
css_button.css("color", "white");
var button_css_style = css_button.attr("class");
//加载并显示cookie字符串
var cookie_string = Base64.encode(JSON.stringify($.cookie()));
textarea_space.val(cookie_string);
textarea_space.attr("value", cookie_string);
//在textarea下方创建复制按钮
var copy_button = createButton("复制", "copy_button", textarea_space, function(){
    //保证cookie_string最新
    cookie_string = Base64.encode(JSON.stringify($.cookie()));
    //复制
    copy(cookie_string);
})
//input_textarea下方设置一个确定按钮
var confirm_button = createButton("确定", "confirm_button", input_textarea_space, function(){
    alert("已尝试设置会话！")
})