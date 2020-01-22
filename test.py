import csv

username = 'dhruv'
amount = 1
users = dict()

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
