import unittest
from libs import HTMLTestRunnerNew
from datetime import datetime
import os
from common.init_data import InitData
from common.constans import REPORTS_DIR, CASES_DIR, INIT_DATA_DIR

if not os.path.exists(INIT_DATA_DIR):
    InitData().generate_user_info()

# 创建测试套件对象
one_suite = unittest.TestSuite()
# 创建测试加载器对象
one_loader = unittest.TestLoader()
# 将测试用例添加到测试套件
# one_suite.addTest(one_loader.loadTestsFromModule(python_0712_homework))
one_suite.addTest(one_loader.discover(start_dir=CASES_DIR, pattern="test*"))
# 创建执行器对象
if not os.path.exists("reports"):
    os.mkdir("reports")
current_time = f"{datetime.now():%Y%m%d%H%M%S}"+".html"
with open(f"{REPORTS_DIR}/report_{current_time}", mode="wb") as write_report:
    one_runner = HTMLTestRunnerNew.HTMLTestRunner(stream=write_report, verbosity=2, title="测试报告", description="副标题", tester="jinbiao")
    one_runner.run(one_suite)

