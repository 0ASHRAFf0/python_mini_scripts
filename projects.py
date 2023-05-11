# Password Generator
import random
import string
import time
from colorama import Fore
# Number Guessing


def factorial(x):
    n = 1
    for i in range(0, x):
        n *= (x-i)
    return n
# print(factorial(7))


def password(length: int = 15):

    global Character
    password = []
    for i in range(length):
        randomLetter = random.choice(string.ascii_letters)
        randomNumber = str(random.randint(0, 9))
        i = random.randint(0, 1)
        if i == 1:
            Character = randomLetter
        elif i == 0:
            Character = randomNumber
        password.append(Character)
    [print(i, end='') for i in password]
# password(15)
##################################################################################################################


def randomize(range: int = 100):
    rightNumber: int = random.randint(1, range)
    Guessing = 0
    Tries = 0
    wrongList = []
    while Guessing != rightNumber:
        randomNumber = random.randint(1, range)
        Guessing = randomNumber
        time.sleep(0.0001)
        if Guessing not in wrongList:
            Tries += 1
            if Guessing == rightNumber:
                print(Fore.GREEN + f"{str(Guessing)}")
                break
            else:
                print(Guessing)
                wrongList.append(Guessing)
        else:
            continue
    if Tries <= 10:
        print(Fore.CYAN + f"{Tries} Tries")
    elif Tries <= 50 and Tries >= 10:
        print(Fore.GREEN + f"{Tries} Tries")
    elif Tries <= 80 and Tries >= 50:
        print(Fore.BLUE + f"{Tries} Tries")
    elif Tries <= 130 and Tries >= 80:
        print(Fore.YELLOW + f"{Tries} Tries")
    elif Tries <= 150 and Tries >= 130:
        print(Fore.RED + f"{Tries} Tries")
    elif Tries >= 150:
        print(Fore.MAGENTA + f"{Tries} Tries")

# randomize(10000)
###################################################################################

# Collatz


def calc(n: int = 0):
    biggest_num = [0]
    nums_to_one = 0
    while n != 1:
        if n < 0:
            return 'Can\'t start with negative number'
        elif n == 0:
            return 'Can\'t start with zero'
        else:
            if n % 2 == 0:
                if n == 2:
                    print(f'{n} --> 1')
                else:
                    print(f'{n} --> ', end='')
                n = int(n/2)
                nums_to_one += 1
                if n > biggest_num[0]:
                    biggest_num.append(n)
            elif n % 2 != 0:
                print(f'{n} --> ', end='')
                n = (n*3) + 1
                nums_to_one += 1
                if n > biggest_num[0]:
                    biggest_num.append(n)
    biggest_num.sort()
    if nums_to_one == 0:
        return 'Can\'t start with one'
    if nums_to_one == 1:
        return 'One Number until reach 1'
    else:
        return f'{nums_to_one} Numbers until reach 1\nBiggest Number In Sequence is {biggest_num[len(biggest_num)-1]}'


# print(calc(126567))


##########################################################################

def filtering(word):
    result = []
    while len(word) != 1:
        if word[0] == word[1]:
            word = word[1:]
        else:
            result.append(word[0])
            word = word[1:]
    else:
        result.append(word[0])
    return ''.join(result)

# print(filtering('wwoorrdd'))

######################################################################################


def sort(input_array: list):
    for i in range(len(input_array)):
        for j in range(i, len(input_array)):
            if input_array[i] > input_array[j]:
                input_array[i], input_array[j] = input_array[j], input_array[i]
    return input_array


def check_elements(input_array: list):
    for i in input_array:
        try:
            float(i)
        except ValueError:
            return ValueError
    sort(input_array)

# print(check_elements([7,6,5,4,3,2,1]))

######################################################################################
