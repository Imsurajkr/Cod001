print("Start")
x = input(print("Is Raining: "))

if x == "yes":
    y = input(print("Have Umbrella ?"))
    if y == "yes":
        print("Go Outside")
    else:
        print("Wait a while")
        y = input(print("Is raining ?"))
        while y == "yes":
            print("wait a while")
            y = input(print("Is raining ?"))
        else:
            print("Go Outside")
else:
    print("Go Outside")