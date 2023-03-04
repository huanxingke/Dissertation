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


chemical_keys = {
    "id": "id",
    "status": "状态码",
    "dangerous_goods_number": "危险化学品编号",
    "cas_number": "CAS号",
    "category": "第一分类",
    "secondary_category": "第二分类",
    "chemical_id": "化学品id",
    "name": "名称",
    "enName": "英文名",
    "weixianxingleibie": "危险类别",
    "xiangxingtu": "象形图",
    "weixianxingshuoming": "危险性说明",
    "lihuatexing": "理化特性",
    "zhuyaoyongtu": "主要用途",
    "ranshaoyubaozhaweixianxing": "燃烧与爆炸危险性",
    "huoxingfanying": "活性反应",
    "jinjiwu": "禁忌物",
    "duxing": "毒性",
    "zhongdubiaoxian": "中毒表现",
    "zhiyejiechuxianzhi": "职业接触限值",
    "huanjingweihai": "环境危害",
    "jijiucuoshi": "急救措施",
    "xielouyingjichuzhi": "泄漏应急处置",
    "miehuofangfa": "灭火方法",
    "ghsType": "化学品统一分类和标签制度来源",
    "ghsjingshici": "警示词",
    "critical_quantity": "环境临界值",
    "similarity": "关键词搜索相似度"
}