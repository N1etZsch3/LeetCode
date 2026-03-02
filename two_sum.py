from typing import List


class solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[num] = i

        return []
