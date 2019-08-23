# @Time :2019/7/24 22:53
# @Author :jinbiao
import logging
from common.operation_config import do_conifg
from common.constans import LOG_DIR


stream_level = do_conifg.get_value(section="LOG", option="stream_level")
file_level = do_conifg.get_value(section="LOG", option="file_level")
log_format = do_conifg.get_value(section="LOG", option="log_format")


class OperationLog:
    """
    操作日志
    """
    def __init__(self, logger_name):
        """
        定义日志对象
        :param logger_name: logger对象名称
        """
        self.logger = logging.getLogger(logger_name)  # 定义日志收集器
        self.logger.setLevel(level=logging.DEBUG)  # 设置收集器的日志级别
        handler_stream = logging.StreamHandler()  # 定义日志输出渠道（控制台）
        handler_file = logging.FileHandler(filename=LOG_DIR, encoding="utf-8")  # 定义日志输出渠道（文件）
        handler_stream.setLevel(level=stream_level)  # 定义渠道日志输出级别
        handler_file.setLevel(level=file_level)
        formatter = logging.Formatter(log_format)  # 格式化日志
        handler_file.setFormatter(formatter)
        handler_stream.setFormatter(formatter)
        self.logger.addHandler(handler_stream)  # 收集器添加渠道
        self.logger.addHandler(handler_file)

    def get_log(self):
        """
        获取日志对象
        :return:日志对象
        """
        print(type(self.logger))
        return self.logger
        pass


log = OperationLog("case").get_log()

if __name__ == '__main__':
    log.error("11111")

