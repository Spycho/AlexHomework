import itertools


max_coins = {
    1: 100,
    2: 50,
    5: 20,
    10: 10,
    20: 5,
    50: 2,
}

values_for_coins = {}

for coin in max_coins.keys():
    max_for_coin = max_coins[coin]
    values_for_coin = []
    for number_coins in range(max_for_coin + 1):
        value_for_coin = coin * number_coins
        values_for_coin.append(value_for_coin)
    values_for_coins[coin] = values_for_coin

product = itertools.product(*values_for_coins.values())

correct_combinations = []
for combination in product:
    if sum(combination) == 100:
        correct_combinations.append(combination)

print(len(correct_combinations))
