nums_e = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def remove_duplicate(nums: list[int]) -> int:

    # 剪枝
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            nums[slow + 1] = nums[fast]
            slow += 1

    return slow + 1


print(remove_duplicate(nums_e))

print(nums_e)
