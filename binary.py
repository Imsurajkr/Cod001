# binary is a base 2 number system
# binary data reading with file
# High level language include binary
# Computer Works on BInary
# Number system based on zeros and one
# for i in range(17):
#     print("{0:>2} in binary is {0:>08b}".format(i))
# or and Xall
# HexaDecimal hex numbers are shorter
# Memory Address
# base 16
# hex digits digits represents 4 binary digits called nibbles
# for i in range(21):
#     print("{0:>2} in hex is {0:>02x}".format(i))
# print("--" * 200)
# x = 0x20
# y = 0x0a
# print(x)
# print(y)
# print(x*y)
# print(0b101010)
# hex 16 power
# Octal - base8
#
#-----------------------------------------------------------------------
# When converting a decomal number to binary, you look for th ehighest power
# of 2 smaller than the number and put a 1 in the next coloumn, you then take the
# remainder and repeat the process with the next highest number power - putting a 1
# have dealt with all powers down to 2** 0 (i.e., 1).
#
# write a programme that requests a number from the keyboard, then prints out
# its binary Representaions
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The programme should carter for numbers up to 65535; i.e (2**16) - 1
#
# Hint: You Will need integer division (//), and modulo (%) to get the remainder
# you will also need ** to raise one number to the power of another:
# for example, 2**8 raises 2 to the power 8
#
# As a optional extra, Avoid printing leading zeros
#
# Once the programme is working, Modify it to print octal rather than binary

powers = []
for power in range(15 , -1, -1):
    powers.append(2 ** power) # for octate change the value to 8

print(powers)

x = int(input("PLease Enter a number: "))

for power in powers:
    print(x // power, end='')
    x %= power

#- ---------------------

printing = False
for power in powers:
    bit = x //power
    if bit != 0  or power == 1:
        printing = True
    if printing:
        print(bit, end='')
        x %= power











































