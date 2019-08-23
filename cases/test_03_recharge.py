# @Time :2019/8/11 21:09
# @Author :jinbiao

from libs.ddt import ddt, data
import unittest
import json
from common.operation_log import log
from common import operation_excel
from common.send_request import do_request
from common.operation_context import OperationContext
from common.constans import EXCEL_DIR
from common.operation_config import do_conifg
from common.operation_mysql import OperationMysql

@ddt
class TestRecharge(unittest.TestCase):
    oe = operation_excel.OperationExcel(EXCEL_DIR, sheet_name="recharge")
    test_data = oe.get_data()
    do_context = OperationContext()
    do_sql = OperationMysql()

    @classmethod
    def setUpClass(cls) -> None:
        log.info("{:-^50}".format("充值模块测试用例开始执行"))

    @classmethod
    def tearDownClass(cls) -> None:
        log.info("{:-^50}".format("充值模块测试用例结束执行"))

    @data(*test_data)
    def test_recharge(self, data):
        url = do_conifg.get_value(section="API", option="url")+data["url"]
        expect = data["expected"]
        check_sql = data["check_sql"]
        if check_sql:
            check_sql = self.do_context.recharge_parameterization(check_sql)
            mysql_data = self.do_sql.get_value(sql=check_sql)
            amount_before = round(float(mysql_data["LeaveAmount"]), 2)
        form_data = self.do_context.recharge_parameterization(data["data"])
        res = do_request.send_request(method=data["method"], url=url,
                                      data=form_data)
        if res.status_code == 200:
            actual = int(res.json()["code"])
            log.info(f"请求地址:{url}\n请求参数:{form_data}\n预期结果:{expect}\n实际结果:{actual}")
            try:
                self.assertEqual(expect, actual)
                if check_sql:
                    mysql_data = self.do_sql.get_value(sql=check_sql)
                    amount_after = round(float(mysql_data["LeaveAmount"]), 2)
                    recharge_amount = json.loads(data["data"])["amount"]
                    expect_amount = amount_before+recharge_amount
                    self.assertEqual(expect_amount, amount_after, msg="充值金额不一致")
                    log.info(f"预期金额:{expect_amount}实际金额:{amount_after}")
                log.info("用例执行通过\n")
                self.oe.write_data(row=data["case_id"]+1, actual=actual, result="PASS")
            except Exception as e:
                log.error(f"用例执行失败{e}\n")
                self.oe.write_data(row=data["case_id"]+1, actual=actual, result="FAIL")
                raise e


if __name__ == '__main__':
    unittest.main()