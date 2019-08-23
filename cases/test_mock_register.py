# @Time :2019/8/4 10:41
# @Author :jinbiao

from libs.ddt import ddt, data
import unittest
from common.operation_log import log
from common import operation_excel
from common.operation_context import OperationContext
from common.constans import EXCEL_DIR
from common.operation_config import do_conifg
from common.send_request import do_request
from unittest.mock import Mock
import json

@ddt
class Register(unittest.TestCase):
    oe = operation_excel.OperationExcel(EXCEL_DIR, sheet_name="register")
    test_data = oe.get_data()
    do_context = OperationContext()
    @staticmethod
    def register(data):
        url = "https://www.jb51.net/article/164055.htm"
        res = do_request.send_request(method="post", url=url, data=data)
        # if res.status_code == 200:
        # if json.loads(res.text["code"]) == "10001" and json.loads(res.text["status"] == 1):
        #     return "注册成功"
        # elif json.loads(res.text["code"]) == "20110" and json.loads(res.text["status"] == 0):
        #     return "手机号码已被注册"
        return res

    def pay(self, data):
        res = self.register(data)
        if json.loads(res)["code"] == "10001" and json.loads(res)["status"] == 1:
            return "注册成功"
        elif json.loads(res.text["code"]) == "20110" and json.loads(res.text["status"] == 0):
            return "手机号码已被注册"


    @data(*test_data)
    def test_register(self, data):
        re = Register()
        form_data = self.do_context.register_parameterization(data["data"])
        status = re.pay(form_data)
        re.register = Mock(return_value='{"status":1,"code":"10001","data":null,"msg":"注册成功"}')

        self.assertEqual(status, "注册成功")

if __name__ == '__main__':
    Register().test_register

