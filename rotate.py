nums_e = [1, 2, 3, 4, 5, 6, 7]
k_e = 3


def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    if k == 0:
        return

    # 反转整个数组
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


rotate(nums_e, k_e)

print(nums_e)
