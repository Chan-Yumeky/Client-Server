# 客户端程序
from socket import *

# 设置服务器的地址和端口号
serverName = '127.0.0.1'
serverPort = 12000

# 创建套接字并连接到服务器
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Connected to server.")

# 保持与服务器的通信
while True:
    # 接收用户输入的消息
    message = input("Your message: ")
    # 将消息编码并发送给服务器
    clientSocket.send(message.encode())

    # 如果用户输入的是"sendfile"
    if message == "sendfile":
        # 请求输入要发送的文件名
        filename = input("Enter filename to send: ")
        # 将文件名编码并发送给服务器
        clientSocket.send(filename.encode())

        # 以二进制只读模式打开文件并读取文件数据
        with open(filename, "rb") as file:
            file_data = file.read()

        # 发送文件数据至服务器
        print("File sent:", filename)

        # 等待服务器端回复
        modifiedSentence = clientSocket.recv(1024)
        print("From server:", modifiedSentence.decode())
        continue

    # 如果用户输入"bye"，则结束通信循环
    elif message.lower() == "bye":
        break

    # 接收并打印来自服务器的修改后的消息
    modifiedSentence = clientSocket.recv(1024)
    print("From server:", modifiedSentence.decode())

# 关闭客户端套接字
clientSocket.close()
