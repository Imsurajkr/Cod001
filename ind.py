#!/usr/bin/python3

import random

highest = 10
answer = random.randint(1, highest)

# answer = 5
print("Please guess a number between 1 and {}:".format(highest))
guess = int(input())

while guess != answer:
    if guess > answer:
        print("Please select lower")
        guess = int(input())
    else:
        print("PLease guess Higher..")
        guess = int(input())

else:
    print("You selected The random number")