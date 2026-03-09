def minCoins(n):

    coins = [10,5,2,1]
    result = []

    for coin in coins:
        while n >= coin:
            n -= coin
            result.append(coin)

    return result


print(minCoins(39))