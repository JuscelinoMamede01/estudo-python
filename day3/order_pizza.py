print("\033[92m*******************************")
print("Welcome to Juscelino's Pizzeria")
print("*******************************\033[0m")


small = 15
medium = 20
large = 25
bill = 0
cheese = 1
pepperoni = 3

print("Let's order your pizza.\n")
size = (input("What's the size of your pizza? S/M/L\n")).upper()
want_pepperoni = (input("Do you want extra pepperoni? Y/N\n")).upper()
want_cheese = (input("Do you want extra cheese? Y/N\n")).upper()

if size == "S":
    pepperoni = 2
    bill = small

    if want_pepperoni == "Y":
        bill = bill + pepperoni
    if want_cheese == "Y":
        bill += cheese
    print(f"\nThe price of your pizza is: \033[92m${bill}\033[0m\n")
elif size == "M":
    bill = medium

    if want_pepperoni == "Y":
        bill = bill + pepperoni
    if want_cheese == "Y":
        bill += cheese
    print(f"\nThe price of your pizza is: \033[92m${bill}\033[0m\n")
else:
    bill = large

    if want_pepperoni == "Y":
        bill = bill + pepperoni
    if want_cheese == "Y":
        bill += cheese

    print(f"\nThe price of your pizza is: \033[92m${bill}\033[0m\n")

print("\033[92m********************************************")
print("Thank you for choosing Juscelino's Pizzeria!")
print("********************************************\033[0m")
