print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?: "))

if height < 120:
    print("You can't play it!")
else:
    age = int(input("What's your age?: "))
    if age < 12:
        print("The Price is $5!")
        print("Enjoy it!")
    elif age < 18:
        print("The Price is $7!")
        print("Enjoy it!")
    else:
        print("The Price is $15!")
        print("Enjoy it!")
