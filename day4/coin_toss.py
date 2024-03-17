import random

coins = ["HEADS", "TAILS"]

coin_random = random.randint(0, 1)
coin_side = coins[coin_random]
print(coin_side)
