# Generate 10 random 12 digit password, then give the option to generate 10 more, or stop
# use condtionals, and loops
# symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~, A-Z, a-z, 0-9

import random



# Generate a random character within the range of !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~, A-Z, a-z, 0-9 (ASCII code 33 - 126) using randint.
# preferred to use chr() since it is built-in rather than concatenate letters and symbols and then perform a random function to select a character.
def generateRandomChar ():
    return chr(random.randint(33, 126))


# Create a 12 didgit password using the random digits generated
def generatePassword():
    digitCount = 12
    password = ''

    for i in range(digitCount):
        password = password + generateRandomChar()
    
    return password

# Generate 10 passwords into a list
def collectPasswords():
    i = 10
    passwordList = []
    while i > 0:
        passwordList.append(generatePassword())
        i -= 1
    # arrange the passwords vertically as a string
    allPasswords = '\n'.join(passwordList)

    return allPasswords


# goAgain() as ternary conditional. Probably more "pythonic" but wanted to illustrate while loop use again too. (see below)
# Also, while loop works better as a base for a more complicated version.

# def goAgain(answer):
#     return  True if answer == "Y" else False if answer == "N" else goAgain(input("What was that? type Y or N: "))


# goAgain() as while loop.
def goAgain(answer):
    while answer != "Y":
        if answer == "N":
            return False
        else:
            answer = input("What was that? type Y or N: ")

    return True 


# theMainFunction() prints passwords, and uses goAgain() ask user whether to continue or not.
def theMainFunction():
    print(collectPasswords())
    again = input("Generate ten more passwords? (Y/N): ")
    
    if goAgain(again): theMainFunction()


theMainFunction()