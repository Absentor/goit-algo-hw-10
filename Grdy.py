import timeit


coins = [50, 25, 10, 5, 2, 1]


# =========================
# Greedy Algorithm
# =========================

def find_coins_greedy(amount):
    result = {}

    for coin in coins:

        count = amount // coin

        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result


# =========================
# Dynamic Programming
# =========================

def find_min_coins(amount):

    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0

    coin_used = [0] * (amount + 1)

    for coin in coins:

        for i in range(coin, amount + 1):

            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}

    while amount > 0:
        coin = coin_used[amount]

        result[coin] = result.get(coin, 0) + 1

        amount -= coin

    return result


# =========================
# Testing
# =========================

amount = 113

print("Greedy:", find_coins_greedy(amount))
print("Dynamic:", find_min_coins(amount))


# =========================
# Time comparison
# =========================

large_amount = 10000

greedy_time = timeit.timeit(
    lambda: find_coins_greedy(large_amount),
    number=1000
)

dynamic_time = timeit.timeit(
    lambda: find_min_coins(large_amount),
    number=1000
)

print(f"\nGreedy time: {greedy_time:.6f} seconds")
print(f"Dynamic programming time: {dynamic_time:.6f} seconds")