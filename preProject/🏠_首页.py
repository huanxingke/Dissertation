import base64
import json

import streamlit as st

from utils.jscode import cookie_manager_jscode

# 一些说明性文字
st.button("首页说明", disabled=True)
st.markdown("""
- 由于\
（1）Streamlit暂无原生的持久化储存api；\
（2）双向组件与页面间的异步通讯会导致千奇百怪的错误；\
（3）课题要求不能使用自己部署的服务器；\
因此暂时先使用「半自动化管理cookie」的方式来存储和读取数据。\n
- 您可以在包括但不限于\
（1）读取您所设置的用户信息；\
（2）读取您的学习与考试记录；\
（3）考试时闪退恢复进度；\
等情况打开本页面，重新手动加载cookie并将其更新至应用会话中。
""")
st.info("注：（1）本程序存储和读取的数据完全基于您的本地计算机，不提供任何的云服务！\
（2）某些浏览器不支持cookie插件，开启隐私模式也可能导致无法使用！")

# 显示 cookie_string
st.text_area(
    # 请勿修改 [Chemical-Cookie]
    label="[Chemical-Cookie]请将以下字符复制于输入框中:",
    key="cookie-string", disabled=True,
    value="这里将存放base64加密的cookie字符串..."
)
# cookie_string输入框
cookie_input = st.text_area(
    # 请勿修改 [Cookie-Input]
    label="[Cookie-Input]请将复制的字符粘贴至下方:",
    placeholder="请复制cookie字符串于此以更新会话状态！",
    key="Cookie-Input"
)

# 执行脚本
st.components.v1.html(html=cookie_manager_jscode, height=0)
# 解密 cookie_string 并加入会话状态
if cookie_input:
    try:
        cookie_input = json.loads(base64.b64decode(cookie_input).decode())
        st.session_state.cookie = cookie_input
        st.success("cookie解密成功！已读取会话！")
    except:
        st.error("cookie字符串解密出错！请检查是否粘贴错误！")
if not st.session_state.get("cookie"):
    st.write("◆ 已设置会话状态：无")
else:
    st.write(" ◆ 已设置会话状态：")
    st.write(st.session_state.get("cookie"))