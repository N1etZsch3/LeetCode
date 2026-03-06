matrix_e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate_t48(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
