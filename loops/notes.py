# Vienna LaRose, Loops Notes in Pyhton

# 1. What is a loop? 
    #A section of code that is going to repeat
# 2. What are the two types of loops?
    #While Loop
x = 0
while x < 10:
    print("Hello", x)
    x +=1 

    #for Loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)
# 3. What is iteration
    #The act of repeting something

# 4. What are lists? 
    #A bunch of values in the same variable
siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tori", "Treyson", "Jeff", "Hailey"]
#print one item from the list
print(siblings[3])
#change an item in a list
siblings[7] = "Jake"
#remove an item from the list
#siblings.pop(5)

# 5. How do you make lists in python? 
    # [] around the list , between each item in the list
    # list items must be proper data types
# 6. How do you make for loops in python? 
#proper list printing with a for loop
num = 1
for sibling in siblings:
    print(f"{num}. {sibling} LaRose")
    num +=1
#using range instead of a list
for num in range(1,11, 2):
    print(num)

# 7. How do you make while loops in python?
import random

num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print(f"Goose!")
        break #Tells the loop to be done
    else:
        print("Duck")
    num += 1

# continue tells the loop to stop that iteration and start again
