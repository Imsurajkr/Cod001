# write a small programme to ask for a name and an age
# write both values have been entered, check if the person
# is the right age to go an 18-30 holiday ( they must be over 18 and under 31)
# if they are , Welcome them to the holiday, Otherwise print
# a polite message refusing them entry

name = input("Please Enter your name :") # its Correct
age = int(input("How old are you, {0} :".format(name))) # Its also correct

# Using the if else condition  Part 1#

# if 18 <= age <= 30: #its correct but trainer used < 31
#     print("Welcome to the club 18-30 Holiday...!! {0}".format(name))
#     print("Hello {0} your entered age is {1}".format(name, age))

# Using the if else 2nd Statement #
#
# if (age >= 18) and (age <= 30): #its correct but trainer used < 31
#     print("Welcome to the Holiday...!!")
#

# Now checking the answers with my solution

# if age >= 18 and age < 31 :
#     print("Welcome to the club 18-30 Holiday...!! {0}".format(name))
# else:
#     print("I m sorry Holiday are for really cool people")
