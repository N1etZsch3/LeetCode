from typing import List

height_example = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    res = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max < right_max:
            res += left_max - height[left]
            left += 1
        else:
            res += right_max - height[right]
            right -= 1

    return res


print(trap(height_example))
