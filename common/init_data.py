# @Time :2019/8/6 22:22
# @Author :jinbiao
from common.send_request import do_request
from common.operation_mysql import OperationMysql
from common.operation_config import do_conifg
from common.constans import INIT_DATA_DIR


class InitData:
    sql = do_conifg.get_value(section="SQL", option="select_user_info")
    url = do_conifg.get_value(section="API", option="url") + "/member/register"
    user_list = eval(do_conifg.get_value(section="INITDATA", option="users"))
    user_info = eval(do_conifg.get_value(section="INITDATA", option="user_info"))

    def create_user(self, regname, pwd="test1234"):
        """
        创建新用户，从配置文件中获取需要获得的用户信息，然后从接口中
        获得这些信息组合成字典
        :param regname: 用户名
        :param pwd: 密码 默认test1234
        :return: 区域名、选项名、选项值组成的嵌套字典的字典
        """
        do_sql = OperationMysql()
        while True:
            mobile = do_sql.create_unregistered_phone()
            data = {"mobilephone": mobile, "pwd": pwd, "regname": regname}
            do_request.send_request(method="post", url=self.url, data=data)
            result = do_sql.get_value(sql=self.sql, args=mobile)
            if result:
                break
        user_info_dict = dict.fromkeys(self.user_info)
        for i in self.user_info:
            value = result[i]
            user_info_dict[i] = value
        user_info_dict["Pwd"] = pwd
        user_dict = {regname: user_info_dict}
        return user_dict
        do_sql.close_db()
        do_request.close()

    def generate_user_info(self):
        """
        生成用户信息，从配置文件中获取要生成的用户名，并将用户信息写入
        初始化数据的配置文件中
        :return:
        """
        for user in self.user_list:
            data = self.create_user(regname=user)
            do_conifg.write_config(filename=INIT_DATA_DIR, datas=data)


if __name__ == '__main__':
    InitData().generate_user_info()
