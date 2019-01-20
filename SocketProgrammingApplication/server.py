# @Author:Dhruv gupta
# Class: CSC 6220
# Homework 2


import socket
import sys

port = 5100;
counter = 0;

#starts by creating a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

# Then bind() is used to associate the socket with the server address.
# In this case, the address is localhost, referring to the current server

serverSocket.bind(('localhost',port));
print('Starting up on ',serverSocket)


#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.
serverSocket.listen(1);
print('the server is ready to receive')
while (counter<10):


    # accept() returns an open connection between the server and client,
    # along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel)
    connectionSocket,clientAddr=serverSocket.accept()

    # Data is read from the connection with recv()
    sentence = connectionSocket.recv(1024).decode()

    capitalizedSentence = sentence.upper()
    counter=counter +1
    print('Recieved: '+ sentence+' Sent: '+ capitalizedSentence)
    print(str(counter)+' chances used. '+ str(10-counter)+ ' chances left')
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
