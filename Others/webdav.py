from Webdav import JianGuoYunClient


jgy = JianGuoYunClient(username="1519657825@qq.com", password="apcdwi4j8zc82vv9")
jgy.login()
text = "我的蓝奏云"
up_res = jgy.upload(content=text.encode(), filename="2.txt")
print(up_res)
remove_res = jgy.remove("2.txt")
print(remove_res)
get_res = jgy.get(filename="2.txt")
print(get_res)
format_res = jgy.format()
print(format_res)