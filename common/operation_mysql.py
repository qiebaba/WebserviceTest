# @Time :2019/8/3 17:41
# @Author :jinbiao

import pymysql
import random
from common.operation_config import do_conifg


class OperationMysql:
    """
    操作mysql数据库
    """
    host = do_conifg.get_value(section="MYSQL", option="host")
    user = do_conifg.get_value(section="MYSQL", option="username")
    pwd = do_conifg.get_value(section="MYSQL", option="password")
    port = do_conifg.get_int_value(section="MYSQL", option="port")
    db = do_conifg.get_value(section="MYSQL", option="database")
    sql = do_conifg.get_value(section="SQL", option="select_user_info")

    def __init__(self):
        """
        初始化实例中的数据库连接和游标对象
        """
        self.db_content = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,
                                          port=self.port,
                                          charset="utf8", cursorclass=pymysql.cursors.DictCursor)   # 定义游标类输出结果为字典
        self.cursor = self.db_content.cursor()

    def get_value(self, sql, args=None, is_all=False):
        """
        获取SQL执行结果
        :param sql: sql语句
        :param args: sql中的参数
        :param is_all:是否返回全部数据
        :return:查询结果
        """
        self.cursor.execute(sql, args=args)
        self.db_content.commit()
        if is_all:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    def close_db(self):
        """
        关闭游标和数据库连接
        :return: None
        """
        self.cursor.close()
        self.db_content.close()

    @staticmethod
    def create_phone():
        """
        随机生成11位的手机号
        :return:返回11位手机号组成的字符串
        """
        roughly = ["136", "137", "138", "158", "188", "180", "139", "133"]
        mantissa = "".join(random.sample("0123456789", 5))
        phone = random.choice(roughly) + mantissa + "456"
        return phone

    def is_existed_phone(self, phone):
        """
        判断手机号在数据库中是否存在，存在返回True，不存在返回False
        :param phone:11位手机号组成的字符串
        :return:Ture or False
        """
        result = self.get_value(sql=self.sql, args=phone)
        if result:
            return True
        else:
            return False

    def create_unregistered_phone(self):
        """
        生成一个随机的手机号，判断它在数据库中是否存在，存在继续重复前面操作，不存在跳出循环，返回手机号
        :return:未注册的手机号（数据库中查不到的手机号）
        """
        while True:
            phone = self.create_phone()
            if not self.is_existed_phone(phone):
                break
        return phone

    def select_registered_phone(self):
        """
        数据库查找已注册的手机号
        :return:未注册的手机号（数据库中查不到的手机号）
        """
        sql = do_conifg.get_value(section="SQL", option="select_registered_phone")
        phone = self.get_value(sql=sql)["MobilePhone"]
        return phone


if __name__ == '__main__':
    mysql = OperationMysql()
    mobile = mysql.select_registered_phone()
    mobile = mysql.create_unregistered_phone()
    print(mobile)
