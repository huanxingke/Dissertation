import base64
import re

try:
    from .webdav4Mod.client import Client
except:
    from webdav4Mod.client import Client


def Validation(func):
    def wrapper(self, *args, **kwargs):
        try:
            if kwargs:
                response = func(self, *args, **kwargs)
            elif args:
                response = func(self, *args)
            else:
                response = func(self)
            return response
        except Exception as error:
            return {"code": -100, "msg": "Error!", "error": str(error)}

    return wrapper


class JianGuoYunClient(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = None

    @Validation
    def login(self):
        self.client = Client(
            base_url="https://dav.jianguoyun.com/dav/",
            auth=(self.username, self.password)
        )
        self.client.mkdir("我的坚果云/EmergencySystemData")
        return {"code": 200}

    @Validation
    def uploadContent(self, content, filename):
        """上传一个文件

        :param bytes content: bytes 形式的文件内容
        :param str filename: 文件名
        :return:
        """
        self.client.upload_content(content=content, to_path=f"我的坚果云/EmergencySystemData/{filename}")
        return {"code": 200, "msg": "Success."}

    @Validation
    def getContent(self, filename):
        """获取一个文件的内容

        :param str filename: 文件名
        :return:
        """
        content = self.client.get_content(path=f"我的坚果云/EmergencySystemData/{filename}")
        return {"code": 200, "msg": "Success.", "content": content}

    @Validation
    def get(self, param, nobase64=False):
        """获取 cookie

        :type nobase64: 是否 base64加密
        :param str param: cookie 键
        :return:
        """
        isStr = lambda x: False if (not isinstance(x, str)) or (not "".join([re.sub(r"\s+", "", i) for i in x])) else True
        if not isStr(param):
            return {"code": -1, "msg": "Key Not Allowed!"}
        param = param.strip()
        if nobase64:
            filename = f"{param}.txt"
        else:
            filename = f"{param}.b64"
        get_result = self.getContent(filename)
        if get_result.get("code") == 200:
            return {"code": 200, "msg": "Success.", "value": get_result.get("content").decode()}
        else:
            return get_result

    @Validation
    def set(self, param, value="", nobase64=False):
        """上传 cookie

        :type nobase64: 是否 base64加密
        :param str param: cookie 键
        :param str value: cookie 值
        :return:
        """
        isStr = lambda x: False if (not isinstance(x, str)) or (not "".join([re.sub(r"\s+", "", i) for i in x])) else True
        if not isStr(param):
            return {"code": -1, "msg": "Key Not Allowed!"}
        param = param.strip()
        if nobase64:
            filename = f"{param}.txt"
            content = str(value).encode()
        else:
            filename = f"{param}.b64"
            content = base64.b64encode(str(value).encode())
        upload_res = self.uploadContent(content=content, filename=filename)
        return upload_res

    @Validation
    def delete(self, param):
        """删除 cookie

        :param str param: cookie 键
        :return:
        """
        isStr = lambda x: False if (not isinstance(x, str)) or (not "".join([re.sub(r"\s+", "", i) for i in x])) else True
        if not isStr(param):
            return {"code": -1, "msg": "Key Not Allowed!"}
        param = param.strip()
        filename = f"{param}.b64"
        delete_result = self.remove(filename)
        return delete_result

    @Validation
    def mkdir(self, dirname):
        """创建一个文件/目录

        :param str dirname: 文件名/目录名
        :return:
        """
        self.client.mkdir(f"我的坚果云/EmergencySystemData/{dirname}")
        return {"code": 200, "msg": "Success."}

    @Validation
    def remove(self, dirname):
        """删除一个文件/目录

        :param dirname: 文件名/目录名
        :return:
        """
        self.client.remove(f"我的坚果云/EmergencySystemData/{dirname}")
        return {"code": 200, "msg": "Success."}

    def format(self):
        """删除 EmergencySystemData 下所有文件

        :return:
        """
        self.client.remove(f"我的坚果云/EmergencySystemData")
        return {"code": 200, "msg": "Success."}