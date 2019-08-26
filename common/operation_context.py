import re
from common.operation_config import OperationConfig, do_conifg
from common.operation_mysql import OperationMysql
from common.constans import INIT_DATA_DIR


class OperationContext:
    """
    参数化测试数据
    """
    init_data_config = OperationConfig(filename=INIT_DATA_DIR)
    unregister_phone_pattern = do_conifg.get_value(section="PARAMETER", option="unregister")
    invest_phone_pattern = do_conifg.get_value(section="PARAMETER", option="invest_user")
    lender_pwd_pattern = do_conifg.get_value(section="PARAMETER", option="lender_pwd")
    admin_phone_pattern = do_conifg.get_value(section="PARAMETER", option="admin_user")
    admin_pwd_pattern = do_conifg.get_value(section="PARAMETER", option="admin_pwd")
    borrower_memberid_pattern = do_conifg.get_value(section="PARAMETER", option="borrower_memberid")
    lender_memberid_pattern = do_conifg.get_value(section="PARAMETER", option="lender_memberid")
    loan_id_pattern = do_conifg.get_value(section="PARAMETER", option="loan_id")
    verify_code_pattern = do_conifg.get_value(section="PARAMETER", option="verify_code")
    send_code_phone_pattern = do_conifg.get_value(section="PARAMETER", option="send_code_phone")

    @classmethod
    def unregister_phone_replace(cls, data):
        """
        未注册手机号的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:已替换手机号的原始字符串
        """
        if re.search(pattern=cls.unregister_phone_pattern, string=data):
            do_mysql = OperationMysql()
            unregistered_phone = do_mysql.create_unregistered_phone()
            data = re.sub(pattern=cls.unregister_phone_pattern, repl=unregistered_phone, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def register_phone_replace(cls, data):
        """
        已注册手机号的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.invest_phone_pattern, string=data):
            do_mysql = OperationMysql()
            registered_phone = cls.init_data_config.get_value(section="lender", option="mobilephone")
            data = re.sub(pattern=cls.invest_phone_pattern, repl=registered_phone, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def lender_pwd_replace(cls, data):
        """
        出借人密码的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.lender_pwd_pattern, string=data):
            do_mysql = OperationMysql()
            lender_pwd = cls.init_data_config.get_value(section="lender", option="pwd")
            data = re.sub(pattern=cls.lender_pwd_pattern, repl=lender_pwd, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def admin_phone_replace(cls, data):
        """
        管理员账号的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.admin_phone_pattern, string=data):
            do_mysql = OperationMysql()
            admin_phone = cls.init_data_config.get_value(section="admin", option="mobilephone")
            data = re.sub(pattern=cls.admin_phone_pattern, repl=admin_phone, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def admin_pwd_replace(cls, data):
        """
        管理员密码的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.admin_pwd_pattern, string=data):
            do_mysql = OperationMysql()
            admin_pwd = cls.init_data_config.get_value(section="admin", option="pwd")
            data = re.sub(pattern=cls.admin_pwd_pattern, repl=admin_pwd, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def borrower_memberid_replace(cls, data):
        """
        借款人id的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.borrower_memberid_pattern, string=data):
            do_mysql = OperationMysql()
            borrower_memberid = cls.init_data_config.get_value(section="borrower", option="id")
            data = re.sub(pattern=cls.borrower_memberid_pattern, repl=borrower_memberid, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def lender_memberid_replace(cls, data):
        """
        出借人id的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.lender_memberid_pattern, string=data):
            do_mysql = OperationMysql()
            lender_memberid = cls.init_data_config.get_value(section="lender", option="id")
            data = re.sub(pattern=cls.lender_memberid_pattern, repl=lender_memberid, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def loan_id_replace(cls, data):
        """
        项目ID的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.loan_id_pattern, string=data):
            do_mysql = OperationMysql()
            loan_id = OperationContext.loan_id
            data = re.sub(pattern=cls.loan_id_pattern, repl=loan_id, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def verify_code_replace(cls, data):
        """
        项目ID的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.verify_code_pattern, string=data):
            do_mysql = OperationMysql()
            verify_code = OperationContext.verify_code
            data = re.sub(pattern=cls.verify_code_pattern, repl=verify_code, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def send_code_phone_replace(cls, data):
        """
        项目ID的参数替换,如果从参数中匹配到模式字符串，则替换，否则不替换
        :param data:原始字符串，data中的data值
        :return:
        """
        if re.search(pattern=cls.send_code_phone_pattern, string=data):
            do_mysql = OperationMysql()
            send_code_phone = OperationContext.send_code_phone
            data = re.sub(pattern=cls.send_code_phone_pattern, repl=send_code_phone, string=data)
            do_mysql.close_db()
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        注册模块用例参数化
        :param data: 原始字符串
        :return: 替换后的字符串
        """
        data = cls.unregister_phone_replace(data)
        data = cls.register_phone_replace(data)
        data = cls.lender_pwd_replace(data)
        data = cls.verify_code_replace(data)
        data = cls.send_code_phone_replace(data)
        return data

    @classmethod
    def login_parameterization(cls, data):
        """
        登录模块用例参数化
        :param data: 原始字符串
        :return: 替换后的字符串
        """
        data = cls.register_phone_replace(data)
        data = cls.lender_pwd_replace(data)
        return data

    @classmethod
    def recharge_parameterization(cls, data):
        """
        充值模块用例参数化
        :param data: 原始字符串
        :return: 替换后的字符串
        """
        data = cls.register_phone_replace(data)
        data = cls.lender_pwd_replace(data)
        return data

    @classmethod
    def add_parameterization(cls, data):
        """
        添加项目用例参数化
        :param data: 原始字符串
        :return: 替换后的字符串
        """
        data = cls.admin_phone_replace(data)
        data = cls.admin_pwd_replace(data)
        data = cls.borrower_memberid_replace(data)
        return data

    @classmethod
    def invest_parameterization(cls, data):
        """
        投资接口用例参数化
        :param data: 原始字符串
        :return: 替换后的字符串
        """
        data = cls.register_phone_replace(data)
        data = cls.lender_pwd_replace(data)
        data = cls.lender_memberid_replace(data)
        data = cls.admin_phone_replace(data)
        data = cls.admin_pwd_replace(data)
        data = cls.borrower_memberid_replace(data)
        data = cls.loan_id_replace(data)
        return data

