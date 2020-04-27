from NetWork.LoginAndReg import *
from NetWork.Retransmission import *
"""
程序入口
"""
s = socketserver.ThreadingTCPServer(ip_port,LoginAndRegister)
s_get = socketserver.ThreadingTCPServer(get_data_ip_and_port,get_data)
phone_send = socketserver.ThreadingTCPServer(send_phone_data_ip_and_port, send_phone_data)
pc_send = socketserver.ThreadingTCPServer(send_pc_data_ip_and_port, send_pc_data)
get_thread = threading.Thread(target=s_get.serve_forever)
phone_send_thread = threading.Thread(target=phone_send.serve_forever)
pc_send_thread = threading.Thread(target=pc_send.serve_forever)
get_thread.start()
phone_send_thread.start()
pc_send_thread.start()
s.serve_forever()

