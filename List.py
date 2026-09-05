import sys 
import os
import random

secret = random.randint(1, 2)

atempt = 0
guessed = False
while guessed == False:
    n = int(input("Guess the number (1, 2): "))
    
    if n == secret:
        print("Good")
        guessed = True
        
        list = [ ]
        s = int(input("Enter the number of elements: "))
        i = 0
        while i < s:
            element = input("Write what you want #" + str(i + 1) + ": ")
            list.append(element)
            i += 1
        print("Your list:", list, "Length:", len(list), "Size:", sys.getsizeof(list), "bytes")
    else:
        atempt += 1
        print("Bad guess. Try again.")
        if atempt >= 3:
            print("noob")
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()