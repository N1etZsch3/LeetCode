nums_e1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

nums_e2 = [5, 4, -1, 7, 8]


def max_subarray(nums: list[int]) -> int:
    cur, res = 0, nums[0]

    for i in range(len(nums)):
        cur = max(nums[i], cur + nums[i])
        res = max(res, cur)

    return res

print(max_subarray(nums_e1))  # 6
print(max_subarray(nums_e2))  # 23
