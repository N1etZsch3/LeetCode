l1 = [
    "RandomizedSet",
    "insert",
    "remove",
    "insert",
    "getRandom",
    "remove",
    "insert",
    "getRandom",
]
l2 = [[], [1], [2], [2], [], [1], [2], []]

import random


class RandomizedSet:

    def __init__(self):
        # 维护两个数据结构
        # 1. 动态数组，用于 O(1) 的随机访问
        self.nums = []
        # 2. 哈希表，用于 O(1) 的查找和定位（Key: 元素值, Value: 在 nums 中的索引）
        self.hash_map = dict()

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False

        # 加入数组尾部
        self.nums.append(val)
        # 记录在哈希表中的索引
        self.hash_map[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        # 1. 获取要删除元素的索引，以及数组的最后一个元素
        index = self.hash_map[val]
        last_element = self.nums[-1]

        # 2. 将最后一个元素的值，覆盖到要删除的元素的位置上
        self.nums[index] = last_element

        # 3. 更新哈希表中 last_element 的索引
        self.hash_map[last_element] = index

        # 4. 【补全】真正执行删除操作
        self.nums.pop()  # 删掉数组最后一位
        del self.hash_map[val]  # 从哈希表中删掉目标元素

        return True

    def getRandom(self) -> int:
        # 直接利用 random.choice 等概率随机获取数组中的元素
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
