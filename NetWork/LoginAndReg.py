from Settings.TCPPortConfiguration import *
from Settings.ResultReply import *
from DataBase.DataBaseDeal import *
import socketserver
import demjson
import DataBase.DataBaseUsing

ip_port=("",PORT_LoginAndRegister)
db = DataBase.DataBaseUsing.DataBaseTool(DataBase_host, DataBase_user, DataBase_password, DataBase_name)
class LoginAndRegister(socketserver.BaseRequestHandler):

    def handle(self):
        print("conn is :", self.request)  # 打印请求
        print("addr is :", self.client_address)  # 打印请求地址
        while True:
            try:
                # 收消息
                data = self.request.recv(1024)
                if not data: break
                try:
                    print(data.decode("utf-8"))
                    AccountINFO = demjson.decode(data.decode("utf-8"))
                    print(AccountINFO)
                except:
                    self.request.sendall(Reply_TypeError)
                print("收到客户端的消息是", data.decode("utf-8"))
                if AccountINFO[RequestType] == LoginType:
                    self.login_try(AccountINFO)
                elif AccountINFO[RequestType] == RegisterType:
                    self.register_try(AccountINFO)
            except Exception as e:
                print(e)
                break

    def register_try(self,account_info):
        reg_name = account_info[AccountUsername]
        reg_num = account_info[AccountNumber]
        reg_passwd = account_info[AccountPassword]
        result = db.set_account(reg_num,reg_name,reg_passwd)
        if result is True:
            self.request.sendall(build_reply("reg_succeed",db.get_account_username(account_info[AccountNumber])).encode())
            print("注册成功")
        elif result is False:
            self.request.sendall(Reply_RegError.encode())
            print("注册失败")



    def login_try(self,account_info):
        if db.get_account_number(account_info[AccountNumber]) and db.get_account_password(account_info[AccountPassword]) is True:
            self.request.sendall(build_reply("login_succeed",db.get_account_username(account_info[AccountNumber])).encode())
            print("登录成功")
        else:
            self.request.sendall(Reply_LoginError.encode())
            print("登录失败")


# if __name__ == "__main__":
#     db = dbuing.DataBaseTool(DataBase_host, DataBase_user, DataBase_password, DataBase_name)
#     s = socketserver.ThreadingTCPServer(ip_port,LoginAndRegister)
#     s.serve_forever()