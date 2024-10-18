# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from socket import *
# --------声明所要发送的服务器端IP地址和监听的端口号------------
serverName = '10.100.3.46'
serverPort = 12000

# ----------之后通过socket提供的接口获取 TCP 对应的socket数据结构---------
# AF_INET指的是用于服务器与服务器之间的网络通信
# SOCK_STREAM指的是基于TCP流式socket通信
clientSocket = socket(AF_INET, SOCK_STREAM)

# -------与对应的客户端发起连接请求，连接完成后，即可进行数据的收发-------------
# 这里使用的connect(address)方法是连接到address处的套接字，
# 一般address的格式为tuple(host,port)，若连接出错，则返回socket.error错误
clientSocket.connect((serverName, serverPort))
# 输出提示字段并将输入的字段存入sentence中
sentence = input('Input sentence:')
# send方法用于发送TCP数据，将sentence中的数据发送到链接的套接字，返回值是要发送的字节数量
clientSocket.send(sentence.encode())
# recv方法用于接受TCP套接字的数据并存入modifiedSentence中，
# 数据以字符串形式返回，传入的参数了指定要接受的最大数据量
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
# 关闭套接字
clientSocket.close()

