# Objeto
# 1. Crie um objeto chamado "pessoa" com as propriedades "nome", "idade" e "endereço" e atribua valores a elas.
pessoa = {"nome": "Juscelino", "idade": 38, "endereco": "Rua sebastiao"}
print(pessoa)
# 2. Acesse o valor da propriedade "nome" do objeto "pessoa".
print(pessoa["nome"])
# 3. Adicione uma nova propriedade chamada "profissao" ao objeto pessoa e atribua um valor a ela.
pessoa["profissao"] = "Engenheiro"
print(pessoa)
# 4. Atualize o valor da propriedade "idade" do objeto pessoa para um novo valor.
pessoa["idade"] = 23
print(pessoa)
# 5. Crie outro objeto chamado "animal" com as propriedades "nome", "especie" e "cor" e atribua valores a elas.
animal = {"nome": "Skye", "especie": "Cachorro", "cor": "Marrom"}
print(animal)
# 6. Crie um objeto chamado "livro" com as propriedades "titulo", "autor" e "ano" e atribua valores a elas.
livro = {"titulo": "Nfl-cincy", "autor": "Joe burrow", "ano": 2015}
# 7. Acesse o valor da propriedade "autor" do objeto livro.
print(f"O autor do livro e: {livro['autor']}")
# 8. Atualize o valor da propriedade "ano" do objeto livro para um novo valor.
livro["ano"]=2019
print(f"O Ano atualizado do livro e: {livro["ano"]}")
# 9. Exclua a propriedade "titulo" do objeto utilizando o operador "delete".
del livro["titulo"]
print(livro)

# 10. Crie um objeto chamado "carro" com as propriedades "marca", "modelo" e "ano" e atribua valores a elas. Em seguida, exiba todas as propriedades do objeto no console.
carro={"marca":"FIAT","modelo":"Uno","ano":2010}
print(carro["marca"])
print(carro["modelo"])
print(carro["ano"])
# 11. Atualize o valor da propriedade "modelo" para "Hyundai" do objeto "carro" e exiba todas as propriedades do objeto no console.
carro["modelo"]="Hyundai"
print(f"O novo modelo do carro e: {carro["modelo"]}")

