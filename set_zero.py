matrix_e = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def set_zero_opt(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    row0_flag = False
    col0_flag = False

    # 1. 判断第一行和第一列是否有 0
    for j in range(n):
        if matrix[0][j] == 0:
            row0_flag = True
            break
    for i in range(m):
        if matrix[i][0] == 0:
            col0_flag = True
            break

    # 2. 用第一行和第一列记录其他行列是否有 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # 3. 根据标记，将对应的元素置为 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # 4. 最后处理第一行和第一列
    if row0_flag:
        for j in range(n):
            matrix[0][j] = 0
    if col0_flag:
        for i in range(m):
            matrix[i][0] = 0
