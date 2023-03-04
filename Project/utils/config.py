import os


# ****** 1.判断应用环境并选择路径 ****** #
# 环境 -> 本地
if os.environ.get("USERDOMAIN") == "HUANXINGKE":
    work_path = os.path.abspath(os.path.dirname(os.getcwd()))
# 环境 -> 云端
else:
    work_path = "."
print(os.path.abspath("."))

# ****** 2.右上角菜单栏 About 文字内容 ****** #
menu_items = {
    "Get Help": "https://github.com/huanxingke/Dissertation",
    "Report a bug": None,
    "About": """
        #### 化工类企业环境事故应急预案演练计算机模拟仿真系统
        - 开发：李文韬 https://github.com/huanxingke
        - 导师：方利国 https://github.com/gzlgfang
        #### Streamlit
    """
}