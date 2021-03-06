#!/usr/bin/env python3

def collatz(num):
    while int(num) > 1:
        if int(num) % 2 == 0:
            num = int(num) // 2
        else:
            num = 3 * int(num) +1
        print(num)
print ("Enter a whole number and press Enter:")
num = input()
collatz(num)
