nums_e = [1, 1, 1, 2, 2, 3]


def remove_duplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    slow = 2

    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


print(remove_duplicates(nums_e))
print(nums_e)
