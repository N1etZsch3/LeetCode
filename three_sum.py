nums_example = [-1, 0, 1, 2, -1, 4]


def three_sum(nums: list[int]) -> list[list[int]]:

    res: list[list[int]] = []

    # 先排序
    nums.sort()

    # 判断首位是否大于零
    if nums[0] > 0:
        return []

    # 遍历数组
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        # 去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                res.append([nums[i], nums[left], nums[right]])
                # 去重
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1

    return res


print(three_sum(nums_example))
print(three_sum([-2, 0, 0, 2, 2]))
