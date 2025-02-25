import socket
import os

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置socket选项,程序退出后立即释放端口资源
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#绑定地址和端口
tcp_server_socket.bind(('127.0.0.1', 8082))
#开始监听
tcp_server_socket.listen(128)

while True:
    try:
        #等待客户端连接
        client_socket, ip_addr = tcp_server_socket.accept()
        data = client_socket.recv(1024)
        file_name = data.decode("utf-8")
        print(file_name, ip_addr)

        #判断文件是否存在
        if os.path.exists('./server' + file_name):
            #读取文件内容
            with open(file_name, 'rb') as f:
                while True:
                    file_data = f.read(1024)
                    if file_data:
                        client_socket.send(file_data)
                    else:
                        break
        else:
            print("文件不存在")
    except Exception as e:
        print(e)
        break
    client_socket.close()

tcp_server_socket.close()




