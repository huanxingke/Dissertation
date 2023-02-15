import os

import streamlit as st
import requests


if os.environ.get("USERDOMAIN") == "HUANXINGKE":
    work_path = os.path.abspath(os.path.dirname(os.getcwd()))
else:
    work_path = "."


# -------------------- README.md -------------------- #
readme_md = os.path.join(work_path, "README.md")
with open(readme_md, "r", encoding="utf-8") as fp:
    st.markdown(fp.read())