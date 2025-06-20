# Password Requirments #

# Atleast 8 Characters Total Long 

# 1 Or More Upper Case Letters
# 1 Or More Lower Case Letters

# 1 Or More Number
# 1 Or More Special Character 


import sys
import time

def main():
    userPass = sys.argv[1]
    authenticate(userPass)

def authenticate(password):
    if len(password) < 8:
        print("length short test")




def buffer(BuffTime,Message):
    time.sleep(BuffTime)
    print(Message)



main()