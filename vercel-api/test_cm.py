import time

import requests


url = "http://192.168.0.103:9000/js2py"
data1 = {
    "uid": "123",
    "platform": "js",
    "result": {
        "cookie": "123"
    }
}
data2 = {
    "uid": "123",
    "platform": "python"
}
response = requests.post(url=url, json=data1).json()
print(response)
for i in range(40):
    response = requests.post(url=url, json=data2).json()
    print(response)
    time.sleep(1)