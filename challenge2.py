#!/usr/bin/python3
import random
highestNumber = 10
answer = random.randint(1, highestNumber)
print("Enter the number betweeen 1 and {}".format(highestNumber))
guess = 0 #initialize to any number outside of the range

while guess != answer:
    guess = int(input())
    if guess > answer:
        print("please Select Lower Number")
        # guess = int(input())
    elif guess < answer:
        print("Please Select Higher Number ")
        # guess = int(input())
    elif guess == 0:
        print("Thanks For playing")
        break
    else:
        print("You guessed it Great")
        break
else:
    print("Great You successfully Guessed on 1st attemp")