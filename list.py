# # ipAddress = input("Please Enter your IP address : ")
# # print = (ipAddress.count("."))
# parrot_list = ["non pinin", "no more", "a stiff", "berfet of live"]
# for state in parrot_list:
#     print(" The parrot is " + state)
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbersInSorted = sorted(numbers)
# print(numbersInSorted)
# print(numbers)
#
# if numbers == numbersInSorted:
#     print("The list are equal")
# else:
#     print("The list ae not equal")
# if numbersInSorted == sorted(numbers):
#     print("The lsit are equal")
# else:
#     print("The list are not equal")




#---------------------------------------------------------------------------------------
# list_1 = []
# list_2 = list()
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
# if list_1 == list_2:
#     print(" The lsit are Equal ")
# print(list("The list are Equal"))
#
# even = [2, 4, 6, 8]
# another_even = sorted(even, reverse=True)
# #print(another_even)
# print(another_even == even)
# another_even.sort(reverse=True)
# print(even)
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)

#------------------------------------------------------------------------------------------
# Challenge Task
# add to the programme below so that if it finds a meal without spam
# it print out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13


menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["span", "egg", "span", "span", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:
    if not "spam" in meal:
       for ingredient in meal:
           print(ingredient)


















