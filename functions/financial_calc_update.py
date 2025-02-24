# Vienna LaRose, Financial Calculator Python

def info(income, amount, type):
    pertype = amount/income*100
    print(f"You spend ${amount:.2f} on {type} and that is {pertype:.0f}% of your income")


# write a print statement telling the user what the program is (Budget calculator)
print("Welcome to my financial calculator. Please follow the instrucitns to learn more about your monthly finances.")
# Ask for monthly income (User input)
income = float(input("What is your monthy income\n"))
# Ask for rent amount (User input)
rent = float(input("What is your monthy rent\n"))
# Ask for utilities amount (User input)
utilites = float(input("What is your monthy utilites\n"))
# Ask for groceries amount (User input)
groceries = float(input("What is your monthy groceries\n"))
# Ask for transportation amount (User input)
transportation = float(input("What is your monthy transportion\n"))
# Calculate savings as 10% of income (variable)
savings = income*.1
# Calcuate spending money income - (rent+utilities+grociers+transportation+savings) (variable)
spending = income - (rent+utilites+groceries+transportation+savings)

info(income, rent, "rent")