from user import User
from random import random

def  main ():
    
    while True:
        print(" Your own password locker a waits")
        print('\n')
        print("kindly select short_code : new user use 'new': for log  'login'or 'exit' for exit:random password 'rnd' ")
        short_code = input().lower()
        print('\n')
        
        if short_code == 'new':
            print("create username")
            create_user_name = input()
            
            print("create password")
            create_password = input()
            
            print("confirm your password")
            confirm_password = input()
            
            
            while confirm_password != create_password:
                print("password invalid")
                print('enter your pasword')
                created_password = input()
                print("confirm your password")
                confirm_password = input()
            
            else:
                print(f"{create_user_name} account creation successful")
                print('\n')
                print("login")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()
            
            while entered_username != create_user_name or entered_password != create_user_name:
                print("invalid username or password")
                print("username")
                entered_username =input()
                print("your password")
                entered_password = input()
                
            while  entered_username != create_user_name or entered_password != created_password:
                print("invalid username or password") 
                print("username") 
                entered_username = input()
                print("Your password")
                entered_password = input()
                
            else:
               print(f"welcome:{entered_username}to your account") 
               print('/n')
                
        elif short_code == 'login':
            print("welcome") 
            print("Enter username")
            default_user_name = input()
            
            print("Enter password")
            default_user_password = input()
            print('\n')
            
            while default_user_name != 'testuser' or default_user_password != '1234':
                print("wrong username or password .Username 'testuser' and password '1234'")
                print("Enter user name")
                default_user_name =input()
                
                print("Enter password")
                default_user_name = input()
                print('\n')
                
            else:
                print("login success") 
                print('\n')   
                print('\n')
                
        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")
            
if __name__== '__main__' :
    main()                   
          