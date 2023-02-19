import base64
import time
import json
import os

import streamlit as st

from components.CookieManager import CookieManager, JSCookieManager

from utils.refreshPage import refreshPage
from utils.actionButton import addActionButton
from utils.queryChemicals import Query
from utils.initUserConfig import initUserConfig

# ---------- Start:每页基础配置 ---------- #
st.set_page_config(page_title="常见危险化学品", page_icon="🧪")
st.markdown("### 🧪 常见危险化学品")
initUserConfig()
# ---------- End:每页基础配置 ---------- #


@st.cache
def load_chemicals():
    with open(os.path.join(st.session_state.work_path, "Data", "jsonfiles", "chemicals.json"), "r") as fp:
        chemicals_data = json.load(fp)
    return chemicals_data


chemicals = None
with st.spinner("正在载入化学品数据..."):
    chemicals = load_chemicals()