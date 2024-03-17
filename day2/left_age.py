import datetime

# Data de nascimento
data_nascimento = datetime.date(1985, 5, 22)

# Data atual
data_atual = datetime.date.today()

# Calcula a diferença em dias entre a data atual e a data de nascimento
diferenca_dias = (data_atual - data_nascimento).days

# Converte a diferença de dias em semanas
semanas_vividas = diferenca_dias // 7

semanas_restantes = 4680 - semanas_vividas

print(
    f"Você já viveu {semanas_vividas} semanas e lhe restaram {semanas_restantes} semanas para completar 90 anos."
)
# resolucao professora

age = int(input("Qual sua idade?:\n"))
age_difference = 90 - age
weeks = age_difference * 52

print(f"Você tem {weeks} semanas restantes")
