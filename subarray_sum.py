from typing import List


nums_example1 = [1, 1, 1]
k1 = 2

nums_example2 = [1, 2, 3]
k2 = 3

nums_example3 = [1, -1, 0]
k3 = 0


def subarray_sum(nums: List[int], k: int) -> int:
    """
    核心公式：前缀和(i-1) = 前缀和(j) - k
    """

    # 设置变量
    pre, count = 0, 0

    # 初始化哈希表
    freq = {0: 1}

    # 遍历：
    for num in nums:
        # 计算当前前缀和
        pre += num

        # 判断公式：
        if pre - k in freq:
            count += freq[pre - k]

        if pre in freq:
            freq[pre] += 1

        else:
            freq[pre] = 1

    return count


print(subarray_sum(nums_example1, k1))

print(subarray_sum(nums_example2, k2))

print(subarray_sum(nums_example3, k3))
