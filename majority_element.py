nums_e = [2, 2, 1, 1, 1, 2, 2]


def majority_element(nums: list[int]) -> int:
    count = 0
    candidate = nums[0]
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]

        if candidate == nums[i]:
            count += 1

        else:
            count -= 1

    return candidate


print(majority_element(nums_e))
