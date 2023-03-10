from .webdav4Mod.client import Client


class JianGuoYunClient(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = None

    def login(self):
        try:
            self.client = Client(
                base_url="https://dav.jianguoyun.com/dav/",
                auth=(self.username, self.password)
            )
            self.client.mkdir("我的坚果云/EmergencySystemData")
            return {"status": 200}
        except Exception as err:
            return {"status": -1, "error": str(err)}

    def upload(self, content, filename):
        """上传一个文件

        :param content: bytes 格式
        :param filename: 文件名
        :return:
        """
        try:
            self.client.upload_content(content=content, to_path=f"我的坚果云/EmergencySystemData/{filename}")
            return {"status": 200}
        except Exception as err:
            return {"status": -1, "error": str(err)}

    def get(self, filename):
        """获取一个文件的内容

        :param filename: 文件名
        :return:
        """
        try:
            content = self.client.get_content(path=f"我的坚果云/EmergencySystemData/{filename}")
            return {"status": 200, "content": content}
        except Exception as err:
            return {"status": -1, "error": str(err)}

    def mkdir(self, dirname):
        """创建一个文件/目录

        :param dirname: 文件名/目录名
        :return:
        """
        try:
            self.client.mkdir(f"我的坚果云/EmergencySystemData/{dirname}")
            return {"status": 200}
        except Exception as err:
            return {"status": -1, "error": str(err)}

    def remove(self, dirname):
        """删除一个文件/目录

        :param dirname: 文件名/目录名
        :return:
        """
        try:
            self.client.remove(f"我的坚果云/EmergencySystemData/{dirname}")
            return {"status": 200}
        except Exception as err:
            return {"status": -1, "error": str(err)}

    def format(self):
        """删除 EmergencySystemData 下所有文件

        :return:
        """
        try:
            self.client.remove(f"我的坚果云/EmergencySystemData")
            return {"status": 200}
        except Exception as err:
            return {"status": -1, "error": str(err)}
