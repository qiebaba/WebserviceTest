from libs.ddt import ddt, data
import unittest
from common.operation_log import log
from common import operation_excel
from common.operation_context import OperationContext
from common.constans import EXCEL_DIR
from common.operation_config import do_conifg
from common.operation_webservice import do_request
import json


@ddt
class TestRegister(unittest.TestCase):
    oe = operation_excel.OperationExcel(EXCEL_DIR, sheet_name="userRegister")
    test_data = oe.get_data()
    do_context = OperationContext()

    @classmethod
    def setUpClass(cls) -> None:
        log.info("{:-^50}".format("注册模块测试用例开始执行"))

    @classmethod
    def tearDownClass(cls) -> None:
        log.info("{:-^50}".format("注册模块测试用例结束执行"))

    @data(*test_data)
    def test_register(self, data):
        url = do_conifg.get_value(section="API", option="url1")+data["url"]
        expect = data["expected"]
        form_data = self.do_context.register_parameterization(data["data"])
        form_data = json.loads(form_data)
        actual = do_request.send_request(url=url, method=data["method"], data=form_data)
        actual = dict(actual)
        actual = str(actual["retInfo"])
        log.info(f"请求地址:{url}\n请求参数:{data}\n逾期结果:{expect}\n实际结果:{actual}")
        try:
            self.assertEqual(expect, actual)
            log.info("用例执行通过\n")
            self.oe.write_data(row=data["case_id"]+1, actual=actual, result="PASS")
        except Exception as e:
            log.error(f"用例执行失败{e}\n")
            self.oe.write_data(row=data["case_id"]+1, actual=actual, result="FAIL")
            raise e


if __name__ == '__main__':
    unittest.main()