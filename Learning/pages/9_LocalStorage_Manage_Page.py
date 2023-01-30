import streamlit as st


st.markdown("""
★&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
本页说明:\n
- 由于\
（1）Streamlit暂无原生的持久化储存api；\
（2）双向组件与页面间的异步通讯会导致千奇百怪的错误；\
（3）课题要求不能使用自己部署的服务器；\
因此暂时先使用「半自动化管理localStorage」的方式来存储和读取数据。\n
- 您可以在包括但不限于\
（1）读取您所设置的用户信息；\
（2）读取您的学习与考试记录；\
（3）考试时闪退恢复进度；\
等情况打开本页面，重新手动加载localStorage并将其更新至应用会话中。
""")
st.info("注：（1）本程序存储和读取的数据完全基于您的本地计算机，不提供任何的云服务！\
（2）某些浏览器不支持localStorage，开启隐私模式也可能导致无法使用！")
st.text_area(
    # 请勿修改 [Chemical-Storage]
    label="[Chemical-Storage]请将以下字符复制于输入框中:",
    key="storage-string", disabled=True,
    value="这里将存放加密的localStorage字符串..."
)
code = """
<head>
    <script src="https://cdn.staticfile.org/jquery/3.4.0/jquery.min.js"></script>
</head>
<body>
    <script>
        //于顶级页面加载js或css
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
                alert("复制成功!")
            } else {
                window.top.document.body.removeChild(copy_element);
                alert("复制失败!请手动复制!")
            }
        }
        
        //生成txt并下载
        function download(filename, text) {
            var element = window.top.document.createElement("a");
            element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
            element.setAttribute("download", filename);
            element.style.display = "none";
            window.top.document.body.appendChild(element);
            element.click();
            window.top.document.body.removeChild(element);
        }
        
        //获取已使用的localStorage容量
        function localStorageUsed() {
          let cache = 0
          for(let key in localStorage) {
            if (localStorage.hasOwnProperty(key)) {
              cache += localStorage.getItem(key).length
            }
          }
          return (cache / 1024).toFixed(2)
        }
        
        //隐藏本组件
        var parent = $(window.frameElement).parent();
        parent.css("display", "none");
        
        //获取根文档
        var root_document = $(window.frameElement).parents("#root");
        
        //显示localStorage容量
        var localStorage_show_p = window.top.document.createElement("p");
        var localStorageUsed_size = localStorageUsed();
        $(localStorage_show_p).text("◆ localStorage容量使用情况：" + localStorageUsed_size + " / 5120 KB")
        var storageString_show_p = root_document.find("p:contains(已设置localStorage)");
        storageString_show_p[0].before(localStorage_show_p);
        
        //获取streamlit按钮样式并隐藏
        var css_button = root_document.find("div.row-widget.stButton").find("button");
        var button_css_style = css_button.attr("class");
        css_button.remove();
        
        //获取textarea元素
        var textarea_div = root_document.find("label:contains(Chemical-Storage)").parent().parent();
        var textarea_space = textarea_div.find("textarea");
        
        //加载并显示localStorage字符串
        var localStorage_string = localStorage.getItem("Chemical-localStorage");
        textarea_space.val(localStorage_string);
        textarea_space.attr("value", localStorage_string);
        
        //在textarea下方创建复制按钮
        var copy_button = window.top.document.createElement("button");
        $(copy_button).attr("kind", "primary");
        $(copy_button).attr("class", button_css_style);
        $(copy_button).text("复制");
        //绑定复制事件
        $(copy_button).click(function(){
            //保持显示的localStorage为最新
            localStorage_string = localStorage.getItem("Chemical-localStorage");
            textarea_space.val(localStorage_string);
            textarea_space.attr("value", localStorage_string);
            localStorageUsed_size = localStorageUsed();
            $(localStorage_show_p).text("◆ localStorage容量使用情况：" + localStorageUsed_size + " / 5120 KB")
            //复制
            copy(localStorage_string);
        });
        textarea_space.after(copy_button);
        
        //再创建一个下载按钮
        var download_button = window.top.document.createElement("button");
        $(download_button).attr("kind", "primary");
        $(download_button).attr("class", button_css_style);
        $(download_button).text("下载");
        //绑定下载事件
        $(download_button).click(function(){
            //保持显示的localStorage为最新
            localStorage_string = localStorage.getItem("Chemical-localStorage");
            textarea_space.val(localStorage_string);
            textarea_space.attr("value", localStorage_string);
            localStorageUsed_size = localStorageUsed();
            $(localStorage_show_p).text("◆ localStorage容量使用情况：" + localStorageUsed_size + " / 5120 KB")
            //下载
            download("Chemical-Storage.txt", localStorage_string);
        });
        copy_button.after(download_button);
        
        //输入框下方设置一个确定按钮
        var input_textarea_div = root_document.find("label:contains(Storage-Input)").parent().parent();
        var input_textarea_space = input_textarea_div.find("textarea");
        var confirm_button = window.top.document.createElement("button");
        $(confirm_button).attr("kind", "primary");
        $(confirm_button).attr("class", button_css_style);
        $(confirm_button).text("确定");
        $(confirm_button).click(function(){
            alert("会话设置成功!")
        });
        input_textarea_space.after(confirm_button);
        
        //再创建一个覆盖按钮
        var overwrite_button = window.top.document.createElement("button");
        $(overwrite_button).attr("kind", "primary");
        $(overwrite_button).attr("class", button_css_style);
        $(overwrite_button).text("覆盖");
        //绑定覆盖事件
        $(overwrite_button).click(function(){
            if (confirm("确定覆盖数据吗？操作不可逆！")) {
                try {
                    localStorage.setItem("Chemical-localStorage", input_textarea_space.text());
                    alert("已覆盖数据！请点击上方复制按钮重新粘贴以更新会话！")
                } catch(err) {
                    alert("覆盖出错！请点击上方复制按钮重新粘贴以更新会话！Error：" + err.message)
                }
            } else {
                alert("已取消覆盖！请重新点击上方复制按钮再次粘贴以恢复会话！")
            }
        });
        confirm_button.after(overwrite_button);
    </script>
</body>
"""
# 用于间接获取按钮样式
st.button("")
# 执行脚本
st.components.v1.html(html=code, height=0)
localStorage_input = st.text_area(
    # 请勿修改 [Storage-Input]
    label="[Storage-Input]请将复制的字符粘贴至下方:",
    placeholder="请复制localStorage字符串于此以更新会话状态！",
    key="storage-input"
)
st.session_state.localStorage = localStorage_input
if not st.session_state.get("localStorage"):
    st.write("◆ 已设置localStorage：无")
else:
    st.write(" ◆已设置localStorage：%s" % st.session_state.localStorage)