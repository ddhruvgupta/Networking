# @Author:Dhruv gupta
# Class: CSC 6220
# Homework 2

import socket
import ast
import csv

counter = 0;
connected =0;
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print ('starting up on: '+ str(server_address))
sock.bind(server_address)

#login
def login(username,password):
    print('user logging in...')
    users = dict()
    # with open("login.json","r") as read_file:
    #     users = json.load(read_file)

    # Opening file with username-password-balance
    with open("users.csv","r") as read_file:
        reader=csv.reader(read_file,delimiter='\t')
        for name,password,balance in reader:
            users.update({name:password})

        if(users.get(username)):
            if(users[username]==password):
                print('login success')
                return 1;
            else:
                print('bad password')
                return -1;
        else:
            print('bad username')
            return 0;

def doSomething(username, data):

    # mod_message = data.decode().upper()
    message = data.decode();
    message = ast.literal_eval(message)
    keys = message.keys()
    for key in keys:
        task = int(key)

    if task !=1:
        amount = int(message[key])

    if(task==2):
        mod_message = Deposit(username,amount);
    elif(task==3):
        mod_message = Withdraw(username,amount);
    elif(task==1):
        mod_message = CurrentBalance(username);


    return mod_message;


def Deposit(username,amount):
    print('deposit in progress...')
    users = dict()
    # with open("accounts.json","r") as read_file:
    #     users = json.load(read_file)
    with open("users.csv","r") as read_file:
        reader=csv.reader(read_file,delimiter='\t')
        for name,password,balance in reader:
            users.update({name:[password,balance] })
    read_file.close()

    users[username][1] = int(users[username][1]) + amount
    print('amount deposited = '+ str(amount))

    with open('users.csv', 'w') as write_file:
        # writer = csv.writer(write_file)
        for key, value in users.items():
           write_file.write(key + "\t" + value[0] + "\t" + str(value[1]) +"\n")
    write_file.close()

    mod_message = "CurrentBalance: " + str(users[username][1])
    return mod_message;

def Withdraw(username,amount):
    users = dict()
    print('Withdraw in progress...')
    with open("users.csv","r") as read_file:
        reader=csv.reader(read_file,delimiter='\t')
        for name,password,balance in reader:
            users.update({name:[password,balance] })
    read_file.close()

    users[username][1] = int(users[username][1]) - amount
    print('amount deposited = '+ str(amount))

    with open('users.csv', 'w') as write_file:
        # writer = csv.writer(write_file)
        for key, value in users.items():
           write_file.write(key + "\t" + value[0] + "\t" + str(value[1]) +"\n")
    write_file.close()

    mod_message = "CurrentBalance: " + str(users[username][1])
    return mod_message;


def CurrentBalance(username):
    users = dict()
    with open("users.csv","r") as read_file:
        reader=csv.reader(read_file,delimiter='\t')
        for name,password,balance in reader:
            users.update({name:[password,balance] })
    read_file.close()

    mod_message = "Current Balance: " + str(users[username][1])
    return mod_message;

while counter<1:
    print ('waiting to receive message')
    data, address = sock.recvfrom(2048)
    # mod_message = data.decode().upper()
    message = data.decode();
    message = ast.literal_eval(message)
    keys = message.keys()
    for key in keys:
        username = key
    password = message[username]

    if login(username,password)==1:
        mod_message = "1"
        sock.sendto(mod_message.encode(), address);
        print ('waiting to receive message')

        while(True):

            data, address = sock.recvfrom(2048)

            message = data.decode();
            message = ast.literal_eval(message)
            keys = message.keys()
            for key in keys:
                task = int(key)

            if task==4:
                break

            mod_message = doSomething(username, data)
            sock.sendto(mod_message.encode(), address);
    else:
        mod_message = "No Access"
        sock.sendto(mod_message.encode(), address);
        counter+=1;

    # print(mod_message)
    # print("data received: "+ data);

    sock.sendto(mod_message.encode(), address);
    counter+=1;
