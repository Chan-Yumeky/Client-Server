# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from socket import *
serverName = '10.100.3.46'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedSentence,serverAddress = clientSocket.recvfrom(2048)
print(modifiedSentence.decode())
clientSocket.close()

