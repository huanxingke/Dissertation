# coding=utf-8
import re

from flask import Flask, request
from flask_caching import Cache


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024
cache = Cache(app, config={"CACHE_TYPE": "simple"})


def isStr(x):
    """判断 x 是否为字符串且不为空

    :param x:
    :return: bool
    """
    return False if (not isinstance(x, str)) or (not "".join([re.sub(r"\s+", "", i) for i in x])) else True


@app.route("/js2py", methods=["POST"])
def js2py():
    """
    (1)在 js 端操作 cookie, 获取操作结果;
    (2)然后携带 uuid 发送操作结果给本接口;
    (3)本接口缓存该操作结果, 限制缓存时间为 30s;
    (4)然后 python 根据该 uuid 轮询该操作结果;
    (5)查询成功后删除该缓存.
    """
    request_dict = request.json
    uid = request_dict.get("uid")
    if not uid:
        return {"code": -1, "msg": "请求参数必须携带 uid 且不能为空!"}
    platform = request_dict.get("platform")
    # js 端
    if platform == "js":
        result = request_dict.get("result")
        if result:
            cache.set(str(uid), result, timeout=30)
            return {"code": 200, "msg": "上传成功!"}
        else:
            return {"code": 0, "msg": "无结果!"}
    # python 端
    elif platform == "python":
        result = cache.get(str(uid))
        if result:
            return {"code": 200, "msg": "获取成功!", "result": result}
        else:
            return {"code": 0, "msg": "无结果!"}
    else:
        return {"code": -1, "msg": "执行端不存在!"}


if __name__ == '__main__':
    app.run("0.0.0.0", 9000)