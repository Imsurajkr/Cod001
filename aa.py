number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0 , len(number)):
    if number[i] in "0123456789":
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))
# Augumentatioin Assessement
x = 23
#adding x
x += 1
print(x)
# Now x = 24

# Subtraction
x -=4
print(x)
# Now x = 20

# Multiplicatioin
x *= 5
print(x)

# Now x = 100

x /= 4
print(x)

# Now x 25

x **= 2
print(x)

# Now x is 625

x %= 60
print(x)

# Now x is 25

greeting = input("Good Morning : ")
greeting += " How was you Day !"
print("hey {}".format(greeting))
greeting *= 5
print(greeting)































