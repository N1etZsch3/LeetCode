import collections

nums_e = [1, 3, -1, -3, 5, 3, 6, 7]
k_e = 3


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # 剪枝
    if k > len(nums):
        return []

    deque = collections.deque()  # 双端队列，用来存储数字的**索引**
    res = []

    for i in range(len(nums)):
        # 1. 维护窗口大小：如果队首的索引已经不在当前的窗口 [i - k + 1, i] 内，弹出队首
        if deque and deque[0] < i - k + 1:
            deque.popleft()

        # 2. 保持队列单调递减：如果当前数字大于队尾索引指向的数字，队尾元素直接淘汰
        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()

        # 3. 把当前数字的索引加入队列
        deque.append(i)

        # 4. 当遍历到第 k 个元素时，开始记录结果
        # 因为队列是单调递减的，队首 deque[0] 永远是当前窗口最大值的索引
        if i >= k - 1:
            res.append(nums[deque[0]])

    return res


print(max_sliding_window(nums_e, k_e))
