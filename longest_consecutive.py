from typing import List

nums_example = [100, 4, 200, 1, 3, 2]


def longest_consecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    max_len = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current = num
            length = 1

            while current + 1 in nums_set:
                current += 1
                length += 1

            max_len = max(max_len, length)

    return max_len


print(longest_consecutive(nums_example))
