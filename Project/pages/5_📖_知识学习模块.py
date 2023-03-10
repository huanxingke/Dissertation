import base64
import os
import re

import streamlit as st
import requests

from utils.initUserConfig import initUserConfig
from utils.learningRate import learningRate
from utils.config import menu_items


def dataFile():
    with open(os.path.join(
            st.session_state.work_path, "Data", "PDF", "{}.pdf".format(st.session_state.get("knowledges_option"))
    ), "rb") as pdf:
        return pdf.read()


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(
    page_title="知识学习模块", page_icon="📖", layout="wide", menu_items=menu_items, initial_sidebar_state="expanded"
)
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    knowledges = [
        i.replace(".md", "") for i in sorted(os.listdir(os.path.join(st.session_state.work_path, "Data", "Knowledges")))
    ]
    with st.sidebar:
        knowledges_option = st.selectbox(
            "选择章节",
            knowledges,
            key="knowledges_option"
        )
        st.radio(
            "切换阅读方式",
            ("Markdown", "图片"),
            horizontal=True,
            key="learning_mode",
        )
        st.markdown("由于Streamlit对Markdown格式支持有限，如有格式错乱可下载PDF后再阅读学习。")
        st.download_button(
            label="下载本节PDF",
            data=dataFile(),
            file_name="{}.pdf".format(st.session_state.get("knowledges_option")),
            mime="application/octet-stream",
        )
    with st.spinner("加载页面"):
        # 以 markdown 方式阅读
        if st.session_state.get("learning_mode") == "Markdown":
            with open(
                    os.path.join(
                        st.session_state.work_path, "Data", "Knowledges",
                        "{}.md".format(st.session_state.get("knowledges_option"))
                    ), "r", encoding="utf-8"
            ) as fp:
                # 这里增加表格与表格间的间距
                knowledge = fp.read().replace("</table>", "</table><br/>")
                # 图片路径
                img_path = os.path.join(st.session_state.work_path, "Data", "Images", "Knowledges", "{}.png")
                # 匹配 md 里的图片链接
                pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
                # 第一项为图片名, 第二项为链接
                for img_name, img_src in pattern.findall(knowledge):
                    # 先还原原文的链接
                    img_link = "![{}]({})".format(img_name, img_src)
                    # 从本地获取图片
                    with open(img_path.format(img_name), "rb") as img:
                        # 然后转换为 base64 链接
                        img_src = f"data:image/png;base64,{base64.b64encode(img.read()).decode()}"
                    # 组合成新的链接
                    new_img_link = "<img style='width:60%' src='{}' alt='{}'/>".format(img_src, img_name)  # "![{}]({})".format(img_name, img_src)
                    # 替换掉原来的链接
                    knowledge = knowledge.replace(img_link, new_img_link)
                st.markdown(knowledge, unsafe_allow_html=True)
                learningRate(chapter_index=knowledges.index(st.session_state.get("knowledges_option")))
        # 以图片方式阅读
        else:
            knowledges_pics_path = os.path.join(
                st.session_state.work_path, "Data", "Images", "KnowledgesPics",
                st.session_state.get("knowledges_option")
            )
            knowledges_pics = sorted(os.listdir(knowledges_pics_path))
            for knowledges_pic in knowledges_pics:
                with open(os.path.join(knowledges_pics_path, knowledges_pic), "rb") as img:
                    st.image(img.read())
            learningRate(chapter_index=knowledges.index(st.session_state.get("knowledges_option")))