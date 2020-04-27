# coding:utf-8

import socket

from multiprocessing import Process


def handle_client(client_socket):
    """
    处理客户端请求
    """
    request_data = client_socket.recv(1024)
    # 接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略

    print("request data:", request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "<h1>HJJ PIG</h1>"
    response = response_start_line + response_headers + "\r\n" + response_body
    client_socket.send(bytes(response, "utf-8"))
    # 向客户端返回响应数据

    client_socket.close()
    # 关闭客户端连接

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # family参数代表地址家族，可为AF_INET或AF_UNIX。AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。
    # type参数代表套接字类型，可为SOCK_STREAM(流套接字，就是TCP套接字)和SOCK_DGRAM(数据报套接字，就是UDP套接字)。
    # 默认为family=AF_INET  type=SOCK_STREM
    # 返回一个整数描述符，用这个描述符来标识这个套接字

    server_socket.bind(("", 8000))
    # 由AF_INET所创建的套接字，address地址必须是一个双元素元组，格式是(host,port)。host代表主机，port代表端口号。
    # 如果端口号正在使用、主机名不正确或端口已被保留，bind方法将引发socket.error异常。

    server_socket.listen(128)
    # backlog指定最多允许多少个客户连接到服务器。它的值至少为1。收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求


    while True:
        client_socket, client_address = server_socket.accept()
        # 调用accept方法时，socket会时入“waiting”状态，也就是处于阻塞状态。客户请求连接时，方法建立连接并返回服务器。
        # accept方法返回一个含有两个元素的元组(connection,address)。
        # 第一个元素connection是所连接的客户端的socket对象（实际上是该对象的内存地址），服务器必须通过它与客户端通信；
        # 第二个元素 address是客户的Internet地址。

        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        # def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        #     group: 分组（基本不用）
        #     target: 表示这个进程实例所调用的对象。
        #     name: 给进程起一个别名
        #     args: 参数，表示调用对象的位置参数元组
        #     kwargs: 表示调用对象的关键字参数字典。

        handle_client_process.start()
        #开始进程