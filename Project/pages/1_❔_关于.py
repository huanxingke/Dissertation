import os

import streamlit as st
import requests


work_path = os.path.abspath(os.path.dirname(os.getcwd()))
st.write(work_path)
readme_md = os.path.join(".", "README.md")
st.write(os.path.exists(readme_md))


# -------------------- README.md -------------------- #
# st.markdown(markdown_readme)