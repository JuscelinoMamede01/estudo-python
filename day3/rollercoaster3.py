print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?: "))
bill = 0

if height < 120:
    print("You can't play it!")
else:
    age = int(input("What's your age?: "))
    if age < 12:
        bill = 5
        print(f"The Price is ${bill}!")
    elif age <= 18:
        bill = 7
        print(f"The Price is ${bill}!")
    else:
        bill = 12
        print(f"The Price is ${bill}!")
    want_photos = input("Do you want photos? Y/N").upper()
    if want_photos == "Y":
        total_bill = bill + 3
        print("The photo's price is $3.")
        print(f"Your total bill is ${total_bill}")
    else:
        print(f"SO,The Price is ${bill}!")
        print("Thank you, and enjoy it!")
