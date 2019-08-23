from libs.ddt import ddt, data
import unittest
from common.operation_log import log
from common import operation_excel
from common.send_request import do_request
from common.operation_context import OperationContext
from common.constans import EXCEL_DIR
from common.operation_config import do_conifg


@ddt
class TestAdd(unittest.TestCase):
    oe = operation_excel.OperationExcel(EXCEL_DIR, sheet_name="add")
    test_data = oe.get_data()
    do_context = OperationContext()

    @classmethod
    def setUpClass(cls) -> None:
        log.info("{:-^50}".format("添加项目接口测试用例开始执行"))

    @classmethod
    def tearDownClass(cls) -> None:
        log.info("{:-^50}".format("添加项目接口测试用例结束执行"))

    @data(*test_data)
    def test_register(self, data):
        url = do_conifg.get_value(section="API", option="url")+data["url"]
        expect = data["expected"]
        form_data = self.do_context.add_parameterization(data["data"])
        res = do_request.send_request(method=data["method"], url=url,
                                      data=form_data)
        log.info(res.text)
        if res.status_code == 200:
            actual = int(res.json()["code"])
            log.info(f"请求地址:{url}\n请求参数:{form_data}\n逾期结果:{expect}\n实际结果:{actual}")
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