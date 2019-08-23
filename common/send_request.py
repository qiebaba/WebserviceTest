import requests
import json


class SendRequest:
    """
    发送接口请求
    """
    def __init__(self):
        self.session = requests.Session()   # 创建session会话

    def send_request(self, method, url, data=None, is_json=False):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                raise e
                data = eval(data)
        method = method.upper()
        if method == "GET":
            res = self.session.get(url=url, params=data)
        elif method == "POST":
            if is_json:
                res = self.session.post(url=url, json=data)
            else:
                res = self.session.post(url=url, data=data)
        return res

    def close(self):
        self.session.close()


do_request = SendRequest()


if __name__ == '__main__':
    register_url = "http://tj.lemonban.com/futureloan/mvc/api/member/register"
    login_url = "http://tj.lemonban.com/futureloan/mvc/api/member/login"
    recharge_url = "http://tj.lemonban.com/futureloan/mvc/api/member/recharge"

    param = {"mobilephone": 13611767797, "pwd": "test1234", "regname": "前额有个旋"}
    login_data = {"mobilephone": 13611767797, "pwd": "test1234"}
    recharge_data = {"mobilephone": 13611767797, "amount": 500000}

    to_request = SendRequest()
    register_result = to_request.send_request("post", register_url, param)
    print(register_result.text)
    login_result = to_request.send_request("post", url=login_url, data=login_data)
    print(login_result.text)
    recharge_result = to_request.send_request("post", url=recharge_url, data=recharge_data)
    print(recharge_result.text)
