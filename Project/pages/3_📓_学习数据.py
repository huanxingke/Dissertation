import json
import os

from matplotlib import font_manager
import matplotlib.pyplot as plt
import streamlit as st

from utils.initUserConfig import initUserConfig
from utils.config import menu_items


@st.cache_data()
def load_chemicals():
    with open(os.path.join(st.session_state.work_path, "Data", "JsonFiles", "chemicals.json"), "r") as fp:
        chemicals_data = json.load(fp)
    return chemicals_data


# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="学习数据", page_icon="📓", layout="wide", menu_items=menu_items)
st.markdown("### 📓 学习数据")
init_result = initUserConfig()
# ---------- End:每页基础配置 ---------- #
# 等待初始化完毕
if init_result:
    # ---------- 以下为页面自定义部分 ---------- #

    # 加载字体
    font = font_manager.FontProperties(
        fname=os.path.join(st.session_state.work_path, "Data", "Fonts", "楷体_GB2312.ttf"),
        size=12
    )

    # 收藏的化学品
    with st.spinner("正在载入化学品数据..."):
        chemicals = load_chemicals()
        chemical_favorites_counts = 0
        if st.session_state.get("chemical_favorites"):
            chemical_favorites = st.session_state.get("chemical_favorites").split(",")[1:]
            chemical_favorites_counts = len(chemical_favorites)
        st.markdown("#### 🧪 已收藏化学品")
        st.slider("已收藏化学品", 0, len(chemicals), chemical_favorites_counts, disabled=True, label_visibility="collapsed")

    # 知识学习进度
    with st.spinner("正在加载学习进度..."):
        knowledges = [
            i.replace(".md", "") for i in sorted(os.listdir(os.path.join(st.session_state.work_path, "Data", "Knowledges")))
        ]
        knowledges_learning_rate = [0 for _ in knowledges]
        if st.session_state.get("learning_cookie"):
            learning_cookie = st.session_state.get("learning_cookie")
            for learning_mode in ["M", "P"]:
                if learning_mode in learning_cookie:
                    learning_cookie_on_mode = learning_cookie[learning_mode]
                    for knowledge_index, knowledge in enumerate(knowledges):
                        if str(knowledge_index) in learning_cookie_on_mode:
                            knowledge_learning_rate = learning_cookie_on_mode[str(knowledge_index)]
                            if knowledge_learning_rate > knowledges_learning_rate[knowledge_index]:
                                knowledges_learning_rate[knowledge_index] = knowledge_learning_rate
        plt.xlim(0, 100)
        ax = plt.gca()
        ax.xaxis.set_major_locator(plt.MultipleLocator(10))
        ax.invert_yaxis()
        plt.yticks(fontproperties=font)
        rects = plt.barh(knowledges, knowledges_learning_rate, height=0.3)
        for rect in rects:
            width = rect.get_width()
            plt.text(width + 1, rect.get_y() + rect.get_height() / 2, f"{width}%", va="center")
        st.markdown("#### 📖 学习进度")
        st.pyplot(fig=plt)
