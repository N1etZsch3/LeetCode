from cmath import inf

prices_e = [7, 1, 5, 3, 6, 4]


def max_profit_2(prices: list[int]) -> int:
    total_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit


print(max_profit_2(prices_e))
