nums_e = [0, 1, 2, 2, 3, 0, 4, 2]
val_e = 2


def remove_element(nums: list[int], val: int) -> int:
    slow, fast = 0, len(nums) - 1

    while slow <= fast:
        if nums[slow] != val:
            slow += 1

        else:
            if nums[fast] == val:
                fast -= 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast -= 1

    return slow


print(remove_element(nums_e, val_e))
