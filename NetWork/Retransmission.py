import socketserver
import threading
from Settings.TCPPortConfiguration import *

# 硬件接收侦听端口
get_data_ip_and_port = ("",PORT_HardWareListen )
# 手机软件发送侦听端口
send_phone_data_ip_and_port = ("", PORT_PhoneListen)
# 电脑软件发送侦听端口
send_pc_data_ip_and_port = ("", PORT_WebListen)
send = ""
phone_trans_data = ""
pc_trans_data = ""
is_phone_data = False
is_pc_data = False
Th_start = False


class get_data(socketserver.BaseRequestHandler):

    def handle(self):
        print("conn is :", self.request)  # 打印请求
        print("addr is :", self.client_address)  # 打印请求地址
        while True:
            try:
                # 收消息
                data = self.request.recv(1024)
                if not data: break
                print(data.decode("utf-8", "ignore"))
                global phone_trans_data
                global pc_trans_data
                global send
                global is_phone_data
                global Th_start
                global is_pc_data
                transData = data.decode("utf-8", "ignore")
                send = transData
                phone_trans_data = send
                pc_trans_data = phone_trans_data
                print(phone_trans_data)
                is_phone_data = True
                is_pc_data = True
                print("收到客户端的消息是", data.decode("utf-8", "ignore"))
                print()

            except Exception as e:
                print(e)
                break


class send_phone_data(socketserver.BaseRequestHandler):

    def handle(self):
        print("conn is :", self.request)  # 打印请求
        print("addr is :", self.client_address)  # 打印请求地址
        print("213")
        global is_phone_data
        while True:
            try:
                if is_phone_data is True:
                    self.request.sendall(phone_trans_data.encode())
                    print("发送的消息是", phone_trans_data)
                    is_phone_data = False
                    break

                elif is_phone_data is False:
                    break

            except Exception as e:
                print(e)
                break


class send_pc_data(socketserver.BaseRequestHandler):

    def handle(self):
        print("conn is :", self.request)  # 打印请求
        print("addr is :", self.client_address)  # 打印请求地址
        print("213")
        global is_pc_data
        while True:
            try:
                if is_pc_data is True:
                    self.request.sendall(pc_trans_data.encode())
                    print("发送的消息是", pc_trans_data)
                    is_pc_data = False
                    break

                elif is_pc_data is False:
                    break

            except Exception as e:
                print(e)
                break


if __name__ == "__main__":
    s_get = socketserver.ThreadingTCPServer(get_data_ip_and_port, get_data)
    phone_send = socketserver.ThreadingTCPServer(send_phone_data_ip_and_port, send_phone_data)
    pc_send = socketserver.ThreadingTCPServer(send_pc_data_ip_and_port, send_pc_data)
    get_thread = threading.Thread(target=s_get.serve_forever)
    phone_send_thread = threading.Thread(target=phone_send.serve_forever)
    pc_send_thread = threading.Thread(target=pc_send.serve_forever)
    get_thread.start()
    phone_send_thread.start()
    pc_send_thread.start()
