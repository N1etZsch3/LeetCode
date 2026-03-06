nums_e1 = [1, 2, 3, 4]
nums_e2 = [-1, 1, 0, -3, 3]


def product_except_self(nums: list[int]) -> list[int]:
    length = len(nums)

    answer: list[int] = [1] * length

    # 1. 计算左侧前缀积（从左向右）
    for i in range(1, length):
        answer[i] = answer[i - 1] * nums[i - 1]

    # 2. 计算右侧后缀积（必须从右向左）
    # 从倒数第二个元素开始：length - 2，一直遍历到 0（包含0，所以步长设为 -1 到 -1 结束）
    r = 1
    for i in range(length - 1, -1, -1):
        answer[i] = answer[i] * r
        r = r * nums[i]

    return answer


print(product_except_self(nums_e1))  # 输出: [24, 12, 8, 6]
print(product_except_self(nums_e2))  # 输出: [0, 0, 9, 0, 0]
