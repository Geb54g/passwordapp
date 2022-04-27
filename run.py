from click import confirm
from user import User

def  main ():
    
    while True:
        print("Welcome to your password locker")
        print('\n')
        print("kindly select short code to navigate through: to create new user use 'nu' ; to log to your account 'lg'or 'ex' to exit ")
        short_code = input().lower()
        print('\n')
        
        if short_code == 'nu':
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
                
        elif short_code == 'lg':
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
          