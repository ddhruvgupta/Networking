import json


with open("login.json","r") as read_file:
    data = json.load(read_file)

print(data['dhruv'])

# data['dummy'] = 'hello'

with open("login.json","w") as write_file:
    json.dump(data,write_file)

if(data.get('dhruv')):
    if(data['dhruv']=='python123'):
        print("found");
else:
    print("not found")
