# @Author:Dhruv gupta
# Class: CSC 6220
# Homework 2

import socket
import json

# Create a UDP socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

print("Welcome to Dhruv's ATM \n")
print("Please login to continue.... ")
username = input("Enter Username: ")
password = input("Enter Password: ")

# Credentials need to sent to the server. For this the need to be encoded into the byte stream
credentials = json.dumps({username:password})
client_sock.sendto(credentials.encode(),server_address)
mod_message, server_address = client_sock.recvfrom(2048)
print ('waiting to receive...')

# rest of the code will only execute if the authentication is successful otherwise fall into
# exit statement

if(mod_message.decode()=='1'):
    while(True):
        print("Welcome " + username)
        print("""Choose from the following options
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. exit""");
        choice = input('Choice: ')
        if choice=='1':
            transaction = json.dumps({choice:0})
            client_sock.sendto(transaction.encode(),server_address)
            print ('waiting to receive')
            mod_message, server_address = client_sock.recvfrom(2048)
            print ('received: ' + mod_message.decode())
        elif choice=='4':
            transaction = json.dumps({choice:0})
            client_sock.sendto(transaction.encode(),server_address)
            print('exiting...')
            client_sock.close()
            exit();
        else:
            amount = input("Amount for Withdraw / Deposit: ")
            transaction = json.dumps({choice:amount})
            client_sock.sendto(transaction.encode(),server_address)
            mod_message, server_address = client_sock.recvfrom(2048)
            print ('received: ' + mod_message.decode())

else:
    print('exiting...')
    exit();


print ('closing socket')
client_sock.close()
