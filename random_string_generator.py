import random

# ASCII RANGE 0-255
#0. NUMBERS asci 10' 48-57
#1. UPPER    65 - 90
#2. LOWER    97 - 122


NUMBER_OF_STRING_SIZE = 0

FINAL_STRING = ""


while NUMBER_OF_STRING_SIZE == 0:
    print('Enter string size bigger then 0: ')
    try:
        NUMBER_OF_STRING_SIZE = int(input())
        print("String size:", NUMBER_OF_STRING_SIZE)
    except ValueError:
        print("Please input integer only...")



while(NUMBER_OF_STRING_SIZE>0):
    random_int = random.randint(0, 2)
    if (random_int == 0):
        random_int = random.randint(48, 57)
        print("Case 0: " + str(random_int))
    elif (random_int ==1):
        random_int = random.randint(65, 90)
        print("Case 1: " + str(random_int))
    elif (random_int ==2):
        random_int = random.randint(97, 122)
        print("Case 2: " + str(random_int))
    else:
        print("Out of range!!")
    FINAL_STRING += chr(random_int)
    NUMBER_OF_STRING_SIZE -=1


print("FINAL STRING: " , FINAL_STRING)