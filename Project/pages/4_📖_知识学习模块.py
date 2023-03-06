import base64
import os
import re

import streamlit as st
import requests

from utils.initUserConfig import initUserConfig
from utils.config import menu_items


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="知识学习模块", page_icon="📖", layout="wide", menu_items=menu_items)
st.markdown("### 📖 知识学习模块")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    knowledges = os.listdir(os.path.join(st.session_state.work_path, "Data", "Knowledges"))
    knowledges_option = st.selectbox(
        "选择章节",
        knowledges,
        key="knowledges_option"
    )
    with st.spinner("加载页面"):
        with open(os.path.join(st.session_state.work_path, "Data", "Knowledges", st.session_state.get("knowledges_option")), "r", encoding="utf-8") as fp:
            # 这里增加表格与表格间的间距
            knowledge = fp.read().replace("</table>", "</table><br/>")
            # 由于 github 最近访问不稳定且资源文件被墙
            # 所以转用了 gitee
            # 但 gitee 存在跨域限制无法直接在网页上访问图片
            # 所以得一张一张在 python 端请求其图片数据
            # 其实可以采用其他免费的图片托管平台: https://postimages.org/
            # 但暂时还是先保留这种方法吧
            while True:
                # 如果 markdown 文本中存在图片
                if pattern.findall(knowledge):
                    # 获取匹配到的第一张图片, 第一项为图片名字, 第二项为图片链接
                    img_items = pattern.findall(knowledge)[0]
                    # 开始以第一张图片分隔整个文本
                    img = f"![{img_items[0]}]({img_items[1]})"
                    knowledge_list = knowledge.split(img)
                    # 首先显示第一项文本内容
                    st.markdown(knowledge_list[0], unsafe_allow_html=True)
                    with st.spinner("加载图片"):
                        # 然后下载图片并显示
                        img_data = requests.get(url=img_items[1]).content
                        if img_data:
                            st.image(img_data)
                        # 然后对剩下的文本继续执行该步骤
                        knowledge = knowledge.replace(knowledge_list[0], "").replace(img, "")
                # 否则直接显示 markdown 文本
                else:
                    st.markdown(knowledge, unsafe_allow_html=True)
                    break