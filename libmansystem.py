# -*- coding: utf-8 -*-
import re
import sqlite3
import subprocess
from student import Student
from distribution import Distribution
import distribution





conn = sqlite3.connect('login.db')
c = conn.cursor() 

def sqllitefile():
    conn = sqlite3.connect('login.db')
    c = conn.cursor() 

class LibManSystem:
    def __init__(self):
        sqllitefile()
        flag = False
        while True:
            print('Register or Login')
            lr = input('Type login or register to continue: ')
            if lr == 'login' or lr == 'Login' or lr == 'LOGIN':
                flag = True
                return login()
            elif lr == 'register' or lr == 'Register' or lr == 'REGISTER':
                flag = True
                return register()
            else:
                print('Please choose either')
                login()
            if flag:
                distribution = Distribution()




# Instructions for registration
def useridins():
    print('--------------------------------------------------------------------------------')
    print('username Instructions:')
    print('Username allows for only alphanumeric characters and must not be more than 15 characters in length')
   


def passwordins():
    print('------------------------------------------------------------------')
    print('Password Instructions:')
    print('1. Password length must be between 5 and 15 \n2. Password must contain atleast one special character')
    print('3. Password must contain atleast one number')
    print('4. Password must contain atleast one upper case character')
    print('5. password must contain atleast one lower case character')



def user_id_check_func(u):
    if re.search("^[a-zA-Z0-9]+$", u) and len(u) >= 6 and len(u) <= 15:
        return True
    else:
        return False



# For conditions in password for registration
def password_check_func(p):
    sc = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
    numbers = '0123456789'
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc = 'abcdefghijklmnopqrstuvwxyz'
    scb, numbers_b, ucb, lcb = False, False, False, False
    for i in range(len(p)):
        if p[i] in sc:
            scb = True
        elif p[i] in numbers:
            numbers_b = True
        elif p[i] in uc:
            ucb = True
        elif p[i] in lc:
            lcb = True
    if scb == numbers_b == ucb == lcb == True:
        return True
    else:
        return False


from distribution import Distribution
# For Password in Login
def login_password():
    # Password
    print('-------------------------------------------------------------------------------------')
    print("Enter any number other than 1 to type password or Enter 1 if you forgot your password")
    pc = input()
    if pc == '1':
        password_id = c.execute("select password from login \
                    where userid = ?", (user_id,)).fetchone()
        print('-----------------------------------------------------------------')
        print(f'Password for the mentioned username - {user_id} is :')
        print(password_id[0])
    else:
        print('--------------------------')
        password = input('Enter Password for login: ')
        password_id_exists = c.execute("SELECT password from login where userid = ? and password = ?", (user_id, password,)).fetchone()
    if password_id_exists:
            print('------------------')
            print('Login Successfull \nWelcome....')
            distribution = Distribution()
            distribution.onFaith()
            distribution.conn.close()
            
    else:
            fl = 0
            print('--------------------------------')
            print('Password is Incorrect, Try again')
            login_password()



# For Registeration
def register():
    # User Name
    nu = True
    while nu:
        useridins()
        print('---------------------------------------')
        user_id = input('Enter your email/username to register: ')
        user_id_check = user_id_check_func(user_id)
        if user_id_check == False:
            print('--------------------------------------')
            print('Read the below instructions carefully:\n')
        else:
            nu = False

    # If user_name already exists
    exist = conn.execute("select USERID from login where USERID like ?", (user_id,)).fetchone()
    if exist:
        print('------------------------------------------')
        print('user_name not available')
        print('Please use different user name to register')
        register()

    # Password
    np = True
    while np:
        passwordins()
        print('----------------------------')
        password = input('Enter password to register: ')
        password_check = password_check_func(password)
        if 5 < len(password) < 16 and password_check:
            np = False
        else:
            print('--------------------------------------')
            print('Read the below instructions carefully:')

    # File Handling
    c.execute("INSERT INTO login (USERID, PASSWORD) \
          VALUES (?, ?)", (user_id, password))
    conn.commit()
    c.close()
    conn.close()
    
    print('------------------------')
    print('congratulation....')
    print('Registration is complete')
    
    
    # For Username in Login
@staticmethod
def login():
    # User Name
    global unchoice
    unchoice, re = 1, 1
    global user_id
    print('------------------------------------')
    user_id = input('Enter username/email to login: ')
    user_id_exists = c.execute("select * from login where USERID like ?", (user_id,)).fetchone()
    if not user_id_exists:
        print('------------------------------------------------------------------')
        print('user name does not exist, Please Register first')
        print('choose 1 to register or choose any other number to try login again')
        unlchoice = input()
        if unlchoice != '1':
            login()
            re = 0
        else:
            unchoice = 0
            register()
    # password
    if unchoice and re:
        login_password()



if __name__ == '__main__':
    LibManSystem()
    
    
    
        
    
    
