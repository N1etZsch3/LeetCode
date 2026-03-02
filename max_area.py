from typing import List


height_example = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def max_area(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    ans = 0

    while l < r:
        left, right = height[l], height[r]
        ans = max(ans, min(left, right) * (r - l))

        if left <= right:
            l += 1
        else:
            r -= 1

    return ans


print(max_area(height_example))
