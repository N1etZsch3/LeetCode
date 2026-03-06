nums_e1 = [2, 3, 1, 1, 4]
nums_e2 = [2, 3, 0, 1, 4]


def jump(nums: list[int]) -> int:
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0
    n = len(nums)

    for i in range(n):

        farthest = max(farthest, nums[i] + i)
        if i == current_end:
            jumps += 1
            current_end = farthest

        if current_end >= n - 1:
            return jumps

    return 0


print(jump(nums_e1))
print(jump(nums_e2))
