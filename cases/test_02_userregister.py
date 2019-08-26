from libs.ddt import ddt, data
import unittest
from common.operation_log import log
from common import operation_excel
from common.operation_context import OperationContext
from common.constans import EXCEL_DIR
from common.operation_config import do_conifg
from common.operation_webservice import do_request
from common.operation_mysql import OperationMysql
import json


@ddt
class TestRegister(unittest.TestCase):
    oe = operation_excel.OperationExcel(EXCEL_DIR, sheet_name="userRegister")
    test_data = oe.get_data()
    do_context = OperationContext()
    do_sql = OperationMysql()

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

        data = json.dumps(data)
        form_data = self.do_context.register_parameterization(data)
        data = json.loads(form_data)
        check_sql = data["check_sql"]
        form_data = json.loads(form_data)
        actual = do_request.send_request(url=url, method=data["method"], data=json.loads(form_data["data"]))
        actual = dict(actual)
        actual = str(actual["retInfo"])
        if check_sql:
            # OperationContext.mobile = str(form_data["mobile"])
            # check_sql = self.do_context.register_parameterization(check_sql)
            mysql_data = self.do_sql.get_value(sql=check_sql)
            OperationContext.verify_code = str(mysql_data["fverify_code"])
            OperationContext.send_code_phone = json.loads(form_data["data"])["mobile"]
            print(json.loads(form_data["data"])["mobile"])

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