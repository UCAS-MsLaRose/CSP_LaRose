# Vienna LaRose, Functions Notes in Pyhton

#Function is an action stored in a key word
#number = int(input("Can I get a number:\n"))
#def add(numOne, numTwo):#parameters go in the parenthesis seperated by commas

    #print(numOne+numTwo)

#add(int(input("Tell me a number:\n")),number)#arguenets are given when the function is called AND must match the number of parameters
#add(2,4)
#add(7,21)

def user(word):
    return input(f"Tell me a {word}:\n")

name = user("name")
verb = user("verb")
place = user("place")
print(f"{name} was {verb} and somehow got to {place}.")