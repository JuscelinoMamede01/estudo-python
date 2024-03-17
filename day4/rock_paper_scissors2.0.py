import random


player_wins = 0
computer_wins = 0
draw = 0

options = ["ROCK", "PAPER", "SCISSORS"]

while True:
    player_input = input("Type ROCK/PAPER/SCISSORS or Q to quit\n").upper()

    if player_input == "Q":
        break

    if player_input not in options:
        print("You need to type ROCK/PAPER/SCISSORS")
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer picked:\n", computer_pick)
    print("You picked:\n", player_input)

    if player_input == computer_pick:
        print("DRAW!")
        draw += 1
    elif player_input == "ROCK" and computer_pick == "SCISSORS":
        print("YOU WON!")
        player_wins += 1

    elif player_input == "PAPER" and computer_pick == "ROCK":
        print("YOU WON!")
        player_wins += 1

    elif player_input == "SCISSORS" and computer_pick == "PAPER":
        print("YOU WON!")
        player_wins += 1
    else:
        print("YOU LOST!")
        computer_wins += 1

print("You won:", player_wins)
print("Computer won:", computer_wins)
print("Draws:", draw)
print("It was FUN! Have a great day!")
