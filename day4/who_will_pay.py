import random

friends = ["Juscelino", "Thais", "Phelipe", "Thalita", "Tony", "Dafany"]
len_friends = len(friends)

# coloque aqui -1 para pois a posicao é de 0 - 5
random_position = random.randint(0, len_friends-1)

who_will_pay = friends[random_position]

print(f"Today is your turn {who_will_pay}!")


fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][2])
