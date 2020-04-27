from DataBase.DataBaseDeal import *
import pymysql
import re
class DataBaseTool:
    def __init__(self,host,user,password,dbname):
        """
        创建数据库连接
        :param host:
        :param user:
        :param password:
        :param dbname:
        """
        self.__connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     db=dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)


    def get_account_number(self,account_number):
        """
        对比当前的账号是在数据库
        :param account_number:
        :return: Bool
        """
        cursor = self.__connection.cursor()
        sql="SELECT " + AccountNumber + " FROM " + Table_name + " WHERE " + AccountNumber + " = " + "\"" + account_number + "\""
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        cursor.close()
        if results == ():
            return False
        elif results[0][AccountNumber] == account_number:
            return True


    def get_account_username(self,account_number):
        """
        对比当前的账号是找到用户名
        :param account_number:
        :return: Bool
        """
        cursor = self.__connection.cursor()
        sql="SELECT " + AccountUsername + " FROM " + Table_name + " WHERE " + AccountNumber + " = " + "\"" + account_number + "\""
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        cursor.close()
        print("完成搜索")
        return results[0][AccountUsername]

    def get_account_password(self,account_password):
        """
        获取当前账号密码
        :param account_password:
        :return: Bool
        """
        cursor = self.__connection.cursor()
        sql="SELECT " + AccountPassword + " FROM " + Table_name + " WHERE " + AccountPassword + " = " + "\"" + account_password + "\""
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        cursor.close()
        if results == ():
            return False
        elif results[0][AccountPassword] == account_password:
            return True

    def set_account(self,account_number,user_name,account_passwd):
        """
        将账号添加到数据库
        :param account_number:
        :param user_name:
        :return: bool
        """

        cursor = self.__connection.cursor()
        sql = " INSERT INTO %s VALUES (\"%s\", \"%s\", \"%s\") " % (Table_name,account_number,user_name,account_passwd)
        print(sql)
        mail_type = re.compile('^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
        x = mail_type.match(account_number)
        if x is not None:
            if x.group() == account_number:
                try:
                    cursor.execute(sql)
                    self.__connection.commit()
                    return True
                except pymysql.err.IntegrityError:
                    return False
                finally:
                    cursor.close()
            else:
                cursor.close()
                return False
        else:
            return False







if __name__ == "__main__":
    db = DataBaseTool(DataBase_host,DataBase_user,DataBase_password,DataBase_name)
    print(db.get_account_number("xsj321@outlook.com"))
    print(db.set_account("1228356491@qq.com","edge"))





