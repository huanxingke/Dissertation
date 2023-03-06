import os


# ****** 1.右上角菜单栏 About 文字内容 ****** #
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

session_state = {
    # 云端、本地、应用会话 三端都有保存的
    "jgy": "坚果云实例",
    "userinfo": "用户个人信息",
    "chemical_favorites": "用户收藏的化学品, 需要用 ',' 来分割成列表",
    "chemicals_query_items": {
        "keywords": "用户上一次搜索化学品的关键词",
        "result": "用户上一次搜索化学品的结果, 是化学品索引组成的列表"
    },
    # 只保存于应用会话的
    # ------ 3_🧪_常见危险化学品.py ------ #
    "chemicals_query_mode": "选择的化学品查询方式",
    "chemicals_all_option": "全部查询时的选项",
    "chemical_favorites_option": "查询收藏时的选项",
    "chemicals_query_option": "关键词查询时的选项"
}