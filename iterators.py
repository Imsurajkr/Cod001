# string = "123456789"
# for char in string:
#     print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# for char in string:
#      print(char)
#
# for char in iter(string):
#     print(char)
#------------------------------------------------------------------------------------------

# Create a list of items ( you may use either strings of numbers in the list )
# then create an iterator using the iter() function
#
# use a for loop to loop "n", times , where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# Hint : use the len() function rather than counting the number of items in the list.
my_list = ["monday", "Tuesday", "thrusday", "friday", "saturday"]
myIter = iter(my_list)
print(myIter)
for i in range(0, len(my_list)):
    print(next(myIter))
