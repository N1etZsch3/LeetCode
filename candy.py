ratings_e1 = [1, 0, 2]
ratings_e2 = [1, 2, 2]


def candy(ratings: list[int]) -> int:
    # 从第二个孩子开始：
    candies = [1] * len(ratings)
    # 从左往右遍历：
    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            candies[i] = candies[i - 1] + 1

    # 从右往左遍历：
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i + 1] < ratings[i]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


print(candy(ratings_e1))
print(candy(ratings_e2))
