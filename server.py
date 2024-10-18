# 服务器端程序
from socket import *

# 设置服务器监听的端口号
serverPort = 12000

# 创建套接字并绑定到指定端口
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# 开始监听传入的连接请求
serverSocket.listen(1)
print('The TCP server is ready to receive')

# 保持接收来自客户端的连接
while True:
    # 接受客户端的连接请求，创建连接套接字和客户端地址
    connectionSocket, addr = serverSocket.accept()
    print("Connected to:", addr)

    # 保持与客户端的通信
    while True:
        # 接收客户端发送的消息
        message = connectionSocket.recv(1024).decode()

        # 如果没有收到消息，即客户端关闭连接，则跳出内层循环
        if not message:
            break

        # 如果客户端发送的消息是"sendfile"
        elif message == "sendfile":
            print("From client:", message)
            # 接收客户端发送的文件名
            filename = connectionSocket.recv(1024).decode()
            # 以二进制只读模式打开文件并读取文件数据
            with open(filename, "rb") as file:
                file_data = file.read()

            # 发送文件数据至客户端
            print("File sent:", filename)
            print("File content:", file_data)
            # 输入服务器端的回复并发送给客户端
            response = input("Your response: ")
            connectionSocket.send(response.encode())
            continue

        # 如果收到客户端的消息是"bye"，则结束当前客户端的通信循环
        elif message == "bye":
            break

        # 打印客户端发送的消息并输入服务器端的回复并发送给客户端
        print("From client:", message)
        response = input("Your response: ")
        connectionSocket.send(response.encode())

    # 关闭连接套接字
    connectionSocket.close()