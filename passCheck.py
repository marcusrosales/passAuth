# Password Requirments #

# Atleast 8 Characters Total Long 

# 1 Or More Upper Case Letters
# 1 Or More Lower Case Letters

# 1 Or More Number
# 1 Or More Special Character 


import sys
import time

passStartingScore = 10


def main():
    userPass = sys.argv[1]

    buffer('initalzing password',3)

    authenticatePassLength(userPass)





def authenticatePassLength(password):
    if len(password) < 8:
        print("length short test")





# Takes in any string message, then stalls the process making by any paramater entered time, to make it feel more cryptic? 
def buffer(Message,BuffTime,):

    print(f" {Message} ")

    for x in range(BuffTime):
        time.sleep(1)
        print('...')

main()