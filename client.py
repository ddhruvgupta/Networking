# @Author:Dhruv gupta
# Class: CSC 6220
# Homework 2


import socket

serverName = 'localhost'
serverPort = 5100;


counter =0

while (counter<10):
    sentence = input("Enter lower case sentence: ")
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(sentence.encode())
    modifiedSentence= clientSocket.recv(1024)
    print('From server:', modifiedSentence.decode())
    clientSocket.close()
    counter=counter+1
    print('chances used(out of 10): '+ str(counter))
