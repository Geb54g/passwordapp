import random

password =("1234567890qwertyuioplkjhgfdsazxcvbnm,./';\#@$%&?QWERTYUIOPLKJHGNMVFCBDXSZA")
password_length = int(input("Enter the length of your password"))
p = "".join(random.sample(password,password_length))

print(f"your generated password is {p}")