# Aqui está como você determina se um ano específico é bissexto:

# Todo ano que for divisível por 4 sem restos,exceto todo ano que for divisível por 100 sem restos,
# A menos que o ano também seja divisível por 400 sem restos.

year = int(input("Type any year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f" {year} is a Leap Year")
        else:
            print(f" {year} is not a Leap Year")
    else:
        print(f" {year} is a Leap Year")
else:
    print(f" {year} is not a Leap Year")
