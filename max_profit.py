from cmath import inf

prices_e = [7, 1, 5, 3, 6, 4]


def max_profit(prices: list[int]) -> int:
    min_price = inf
    max_profit_v = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit_v = max(price - min_price, max_profit_v)

    return max_profit_v


print(max_profit(prices_e))
