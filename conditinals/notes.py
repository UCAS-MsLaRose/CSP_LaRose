# Vienna LaRose, Conditionals notes Python

#print("Hello, welcome to my program that will sort you into a category.")

#name = input("What is your name:\n")

#if name == "Vienna":
    #print("Oh your the teacher. . . never mind.")
#else:
    #print("You are a student. Welcome to class.")


"""
num = int(input("how many would you like:(give me a number above 0)\n"))

if num == 1:
    #print("You have asked for an item")
elif num <= 3:
    print("You have asked for a couple of the item.")
elif num <= 5:
    print("You have asked for a few of the item. . .or your in the south and you asked for a couple.")
else:
    print("You have asked for some of the item.")
"""

"""name = "Katie"

if "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
    print("Your name has a vowel!")
else:
    print("Your name dosn't have a vowel.")
"""

num = 6

if num > 5 and num < 10:
    if num == 7:
        print(f"{num} is an unluck number!")
    else:
        print(f"{num} is a large single digit number")
else:
    if num == 4:
        print(f"{num} is the best number!")
    else:
        if num >= 10:
            print(f"{num} is not a single digit number")
        else:
            print(f"{num} is a small number")