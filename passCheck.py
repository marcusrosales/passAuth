# Password Requirments #

# Atleast 8 Characters Total Long 

# 1 Or More Upper Case Letters
# 1 Or More Lower Case Letters

# 1 Or More Number
# 1 Or More Special Character 


import sys
import time



def main():
    totalScore = 0

    userPass = sys.argv[1]

    buffer('Initalzing Password\n',2)
    totalScore += authenticatePassLength(userPass)

    buffer('Checking For Uppercased Characters\n',2)
    totalScore += authenticateForLoudLetters(userPass)

    buffer('Checking For Lowercased Characters\n',2)
    totalScore += authenticateForLowerLetters(userPass)

    buffer('Checking For Digits In Password\n',2)
    totalScore += authenticateForNums(userPass)

    buffer('Checking For Special Characters In Password\n',2)
    totalScore += authenticateForSpecialChars(userPass)

    print(f"\nFinal Password Strength Score: {totalScore}/10\n")



def authenticatePassLength(password):
    print("Starting Passcode Length Authentication Process")
    if len(password) < 8:
        print('\nProcess Failed. +0\n')
        return(0)
    else:
        print('\nProcess Passed. +2\n')
        return(2)
    


def authenticateForLoudLetters(password):
    for char in password:
        if char.isupper():
            print('\nProcess Passed. +2\n')
            return(2)
        else:
            print('\nProcess Failed. +0\n')
            return(0)

def authenticateForLowerLetters(password):
    for char in password:
        if char.islower():
            print('\nProcess Passed. +2\n')
            return(2)
        else:
            print('\nProcess Failed. +0\n')
            return(0)



def authenticateForNums(password):
    for char in password:
        if char.isdigit():
            print('\nProcess Passed. +2\n')
            return(2)
        else:
            print('\nProcess Failed. +0\n')
            return(0)
        

def authenticateForSpecialChars(password):
    specList = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','[',']','}','{',';',':',]
    for char in password:
        if char in specList:
            print('\nProcess Passed. +2\n')
            return(2)
        else:
            print('\nProcess Failed. +0\n')
            return(0)



# Takes in any string message, then stalls the process making by any paramater entered time, to make it feel more cryptic? 
def buffer(Message,BuffTime,):

    print(f"{Message}")

    for x in range(BuffTime):
        time.sleep(1)
        print('\n...\n')

main()