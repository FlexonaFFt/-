def count_ways_to_make_change(amount, denominations):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in denominations:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]

amount = int(input())
n = int(input())
denominations = list(map(int, input().split()))
print(count_ways_to_make_change(amount, denominations))