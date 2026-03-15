def minCost(coins, k):

    coins.sort()

    i = 0
    j = len(coins) - 1

    cost = 0

    while i <= j:
        cost += coins[i]   # buy cheapest coin
        i += 1

        j -= k   # take k most expensive coins free

    return cost


# Function Call
coins = [1,2,3,4]
k = 2

print(minCost(coins, k))