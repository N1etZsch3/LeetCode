from typing import List

nums_example = [2, 1, 0, 3, 12]


def move_zeroes(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
