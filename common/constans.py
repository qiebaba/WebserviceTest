# @Time :2019/8/6 22:30
# @Author :jinbiao
import os

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件目录
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
# 配置文件
CONFIG_DIR = os.path.join(CONFIGS_DIR, "config.ini")
# 初始化测试数据配置文件
INIT_DATA_DIR = os.path.join(CONFIGS_DIR, "init_data.ini")
# 数据文件目录
DATAS_DIR = os.path.join(BASE_DIR, "datas")
# 数据文件
EXCEL_DIR = os.path.join(DATAS_DIR, "cases.xlsx")
# 日志目录
LOGS_DIR = os.path.join(BASE_DIR, "logs")
# 日志文件
LOG_DIR = os.path.join(LOGS_DIR, "api_test.log")
# 测试报告目录
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
# 测试用例目录
CASES_DIR = os.path.join(BASE_DIR, "cases")

