import json
import os

with open('./user.json') as json_file:
    data = json.load(json_file)
def Register():
    print("""
    1)Login As Admin
    2)Login As Student
    """)
Register()
Admin = ''
student = ''
l_x = input('Enter A number\n:')
if l_x == '1':
    user = input('Enter Admin UserName: ')
    password = input('Enter Admin Password: ')
    while user != data['admin']['userName']:
        user = input('Enter Admin UserName: ')
    while password != data['admin']['password']:
        password = input('Enter Admin Password: ')
    Admin = True

    
            

    
elif l_x == '2':
    user = input('Enter Student UserName: ')
    password = input('Enter Student Password: ')
    while user != data['students']['userName'] and password != data['studnets']['password']:
        user = input('Enter Admin UserName: ')
        password = input('Enter Admin Password: ')
    student = True
        
            

    





