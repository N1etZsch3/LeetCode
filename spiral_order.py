matrix_e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while True:
        # 1. 向右走：遍历上边界的这一行
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1  # 走完上边界，上边界收缩（下移）
        if top > bottom:  # 检查是否越界
            break

        # 2. 向下走：遍历右边界的这一列
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1  # 走完右边界，右边界收缩（左移）
        if left > right:
            break

        # 3. 向左走：遍历下边界的这一行
        # 注意 range 的步长是 -1，倒着走
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1  # 走完下边界，下边界收缩（上移）
        if top > bottom:
            break

        # 4. 向上走：遍历左边界的这一列
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1  # 走完左边界，左边界收缩（右移）
        if left > right:
            break

    return res
