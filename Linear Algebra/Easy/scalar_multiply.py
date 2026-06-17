def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] * scalar
    return result
print(scalar_multiply(matrix = [[1, 2], [3, 4]], scalar = 2))