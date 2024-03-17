# Array
# 1. Crie um array vazio chamado "numeros".
numeros = []
# 2. Adicione os números 1, 2, 3 e 4 ao array "numeros".
numeros = [1, 2, 3, 4, 5]
# 3. Acesse o valor do segundo elemento do array "numeros".
print(numeros[1])
# 4. Atualize o valor do terceiro elemento do array "numeros" para 10.
numeros[2] = 10
print(numeros)
# 5. Remova o último elemento do array "numeros" utilizando a função ".pop".
numeros.pop()
print(numeros)
# 6. Verifique o comprimento do array "numeros".
numeros_length = len(numeros)
print(f"o array possui {numeros_length} elementos")
# 7. Crie um novo array chamado "frutas" contendo as strings "maçã", "banana" e "laranja".
frutas = ["Maca", "Banana", "Laranja"]
print(frutas)
# 8. Acesse o valor do primeiro elemento do array frutas.
print(frutas[0])
# 9. Adicione a string "uva" ao final do array frutas utilizando a função ".push".
frutas.append("Uva")
print(frutas)

# 10. Crie um objeto chamado "aluno" com as propriedades "nome" e "idade" e atribua valores a elas. Em seguida, crie um array chamado "alunos" e adicione o objeto "aluno" a esse array.

aluno = {"nome": "Juscelino", "idade": 38}

alunos = []
alunos.append(aluno)
# outra forma de add um aluno no objeto
alunos.append({"nome": "Joao", "idade": 30})

print(alunos)

# 11. Acesse o valor da propriedade "nome" do primeiro elemento do array "alunos".
print(alunos[1]["nome"])
# 12. Adicione mais três objetos do tipo "aluno" ao array "alunos".
alunos.append({"nome": "Jose", "idade": 28})
alunos.append({"nome": "Fernando", "idade": 33})
alunos.append({"nome": "Felipe", "idade": 45})
print(alunos)

# 13. Crie um array chamando "produtos" contendo 10 produtos de supermercado. Em seguida, exiba no terminal apenas os produtos que ficaram em posições pares.
produtos = [
    "Arroz",
    "Feijao",
    "Macarrao",
    "Oleo de cozinha",
    "Leite",
    "Ovos",
    "Carne",
    "Frutas",
    "Legumes",
    "Pao"
]
print(
    f"Os produtos das posições pares são:\n{produtos[2]}\n{produtos[4]}\n{produtos[4]}\n{produtos[6]}\n{produtos[8]}")
