# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from socket import *
# ---------设定端口号为12000，获取 TCP 对应的链接，并且将端口号和 TCP socket 绑定，并设定监听值--------
# AF_INET指的是用于服务器与服务器之间的网络通信
# SOCK_STREAM指的是基于TCP流式socket通信
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
# bind方法是将套接字绑定到地址，在AF_INET协议下，以tuple(host,port)的方式传入，
# 其中host为绑定的地址，port为监听的端口
serverSocket.bind(('',serverPort))
# listen方法是开始监听TCP传入连接，传入的参数指定在拒绝连接前，
# 操作系统可以挂起的最大连接数，该值最少为1，通常设为5
serverSocket.listen(1)

# --------while循环，接受客户端发来的链接，并且调用 send 和 recv 接口进行信息的传递-------
print('The Tcp server is ready to recieve')
while True:
    # 这里的accept方法接受TCP链接并返回元组（conn,address），
    # 其中conn是新的套接字对象，可以用来接收和发送数据，address是链接客户端的地址
    connectionSocket, addr = serverSocket.accept()
    # recv方法用于接受TCP套接字的数据并存入sentence中，
    # 数据以字符串形式返回，传入的参数了指定要接受的最大数据量
    sentence = connectionSocket.recv(1024).decode()
    # 输出客户端发送的字符串以及客户端的地址
    print(sentence)
    print(addr)
    # 这一句代码是将客户端发送的字符串做修改并存入capitalizedSentence中
    capitalizedSentence = sentence[2:6] + ("-received message")
    # send方法用于发送TCP数据，将capitalizedSentence中的数据发送到链接的套接字，
    # 返回值是要发送的字节数量
    connectionSocket.send(capitalizedSentence.encode())
    # 关闭套接字
    connectionSocket.close()


