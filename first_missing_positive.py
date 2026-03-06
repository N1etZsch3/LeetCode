nums_e = [3, 4, -1, 1]


def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)

    for i in range(n):
        # 1. 必须在 while 循环中判断：
        # - 数字是否在 [1, n] 的有效范围内
        # - 目标位置上的数字是不是已经被正确放置了（防止重复元素死循环）
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            # 2. 提前计算目标索引，避开 Python 连等赋值的陷阱
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]

    # 3. 再次遍历找茬
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # 4. 如果全对上了，说明缺的是最大的下一个数
    return n + 1


print(first_missing_positive(nums_e))  # 输出: 2
