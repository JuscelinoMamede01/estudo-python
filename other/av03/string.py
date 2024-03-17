# * String
# 1. Crie uma variável chamada "nome" e atribua a ela uma string com seu nome. Em seguida, exiba o conteúdo da variável "nome" no terminal.
nome = "Juscelino"
print(nome)
# 2. Crie uma variável chamada "frase" e atribua a ela uma frase de sua escolha. Em seguida, exiba o comprimento da string armazenada na variável "frase".
frase = "Juscelino esta aprendendo Python"
frase_length = len(frase)
print(f"A frase possui um total de: {frase_length}")


# 3. Crie uma variável chamada "palavra" e atribua a ela uma palavra qualquer. Em seguida, exiba a primeira letra da palavra armazenada na variável "palavra".
palavra = "Macarrao"
print(f"A primeira letra da palavra digitada e: {palavra[0]}")
# 4. Crie uma variável chamada "frase" e atribua a ela uma frase de sua escolha. Em seguida, exiba a frase em letras maiusculas.
frase2 = "Juscelino esta aprendendo Python"
capital_frase = frase2.upper()
print(capital_frase)

# 5. Crie uma variável chamada "endereço" e atribua a ela um valor de sua escolha. Em seguida, sobrescreva o valor da variável para um outro endereço e verifique no terminal o valor atual da variável.
endereco = "Rua Parnamirim 25"
endereco = "Rua Sebastiao 36"
print(endereco)
