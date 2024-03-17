import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

print('''
  _____         _             _____                 _   _______                              
 |  __ \       | |           |  __ \               | | |__   __|                             
 | |__) |__  __| |_ __ __ _  | |__) |_ _ _ __   ___| |    | | ___  ___  ___  _   _ _ __ __ _ 
 |  ___/ _ \/ _` | '__/ _` | |  ___/ _` | '_ \ / _ \ |    | |/ _ \/ __|/ _ \| | | | '__/ _` |
 | |  |  __/ (_| | | | (_| | | |  | (_| | |_) |  __/ |    | |  __/\__ \ (_) | |_| | | | (_| |
 |_|   \___|\__,_|_|  \__,_| |_|   \__,_| .__/ \___|_|    |_|\___||___/\___/ \__,_|_|  \__,_|
                                        | |                                                  
                                        |_|                                                  
''')
player_name = input("Qual o seu nome?: ")
print(f"\n\nOlá,{player_name}! Eu te desafio a me vencer. VAMOS JOGAR!\n")
player_pick = int(input("Escolha uma opção:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
number_options = len(options)
random_position = random.randint(0, number_options-1)
computer_pick = options[random_position]

if player_pick == 1:
    print("Sua escolha foi:\n", rock)
    print("O computador escolheu:\n", computer_pick)
    if computer_pick == rock:
        print("O jogo EMPATOU")
    elif computer_pick == paper:
        print("Voce Perdeu")
    else:
        print("Voce Venceu")

elif player_pick == 2:
    print("Sua escolha foi:\n", paper)
    print("O computador escolheu:\n", computer_pick)
    if computer_pick == paper:
        print("O jogo EMPATOU")
    elif computer_pick == scissors:
        print("Voce Perdeu")
    else:
        print("Voce Venceu")
elif player_pick == 3:
    print("Sua escolha foi:\n", scissors)
    print("O computador escolheu:\n", computer_pick)
    if computer_pick == scissors:
        print("O jogo EMPATOU")
    elif computer_pick == rock:
        print("Voce Perdeu")
    else:
        print("Voce Venceu")
else:
    print("Voce precisa escolher uma das opções válidas!")
