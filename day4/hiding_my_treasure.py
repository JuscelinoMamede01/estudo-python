line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]


map = [line1, line2, line3]

print("Esconda seu tesouro escrevendo a posicao no MAPA.\nEX: A3\nAs letras precisam ser A,B ou C e os numeros de 1,2 ou 3")

position = input("Onde voce deseja esconder seu tesouro:\n")

letter = position[0].lower()  # letra
abc = ["a", "b", "c"]
# o .index retorna o indice da primeira ocorrencia de letter
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[letter_index][number_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
