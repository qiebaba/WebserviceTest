from configparser import ConfigParser
from common.constans import CONFIG_DIR


class OperationConfig:
    """
    操作配置文件
    """
    def __init__(self, filename):
        """
        构造方法，初始化配置文件路径、参数配置操作
        :param filename: 配置文件路径
        """
        self.filename = filename
        self.cp = ConfigParser()
        self.cp.read(self.filename, encoding="utf-8")

    def get_value(self, section, option):
        """
        获取str类型的选项值
        :param section: 区域名
        :param option: 选项名
        :return: 选项值
        """
        return self.cp.get(section, option)

    def get_int_value(self, section, option):
        """
        获取int类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.cp.getint(section, option)

    def get_float_value(self, section, option):
        """
        获取float类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.cp.getfloat(section, option)

    def get_bool_value(self, section, option):
        """
        获取bool类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.cp.getboolean(section, option)

    def get_eval_value(self, section, option):
        """
        返回执行表达式后的值
        :param section:
        :param option:
        :return:
        """
        return eval(self.cp.get(section, option))

    @staticmethod
    def write_config(filename, datas):
        """
        写入配置文件
        :param filename: 配置文件
        :return: None
        """
        cp = ConfigParser()
        if isinstance(datas, dict):
            for key in datas:
                if not isinstance(datas[key], dict):
                    return "配置文件数据格式错误"
                cp[key] = datas[key]
            with open(file=filename, mode="a", encoding="utf-8") as write_config:
                cp.write(write_config)
        else:
            print("配置文件数据格式错误")


do_conifg = OperationConfig(filename=CONFIG_DIR)


if __name__ == '__main__':
    value = do_conifg.get_value(section="EXCEL", option="url")
    print(value)
    # config_data = {"EXCEL": {"case_id": 1}, "PATH": {"excelpath": "test_data.xlsx"}}
    # do_conifg.write_config(filename="test.ini", datas=config_data)
