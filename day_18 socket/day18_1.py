import socket

# 创建 TCP socket
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
tcp_client_socket.connect(('127.0.0.1', 8082))

# 获取文件名，并编码为 utf-8 格式
file_name = input("请输入要发送的文件名：")
file_name_code = file_name.encode("utf-8")

# 发送文件名
tcp_client_socket.send(file_name_code)

# 获取服务端文件内容
with open("./client/" + file_name, "wb") as file:
    while True:
        file_date =tcp_client_socket.recv(1024)
        if file_date:
            file.write(file_date)
        else:
            break

tcp_client_socket.close()
















