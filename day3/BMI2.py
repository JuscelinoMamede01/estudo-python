weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f}")
    print(f"You are in Underweight level")
elif 18.5 <= BMI <= 24.9:
    print(f"Your BMI is {BMI:.2f}")
    print(f"You are in Normal weight level")
elif 25.0 <= BMI <= 29.9:
    print(f"Your BMI is {BMI:.2f}")
    print(f"You are in Overweight level")
else:
    if 30.0 <= BMI <= 34.9:
        print(f"Your BMI is {BMI:.2f}")
        print(f"You are in Obesity grade1")

    elif 35.0 <= BMI <= 39.9:
        print(f"Your BMI is {BMI:.2f}")
        print(f"You are in Obesity grade2")

    else:
        print(f"Your BMI is {BMI:.2f}")
        print(f"You are in Obesity grade3")
