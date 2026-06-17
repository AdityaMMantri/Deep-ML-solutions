def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    rows=len(matrix)
    cols=len(matrix[0])
    means=[]

    if mode=="row":
        for i in range(rows):
            row_sum=0.0
            for j in range(cols):
                row_sum+=matrix[i][j]
            means.append(row_sum/cols)

    elif mode=="column":
        for j in range(cols):
            col_sum=0.0
            for i in range(rows):
                col_sum+=matrix[i][j]
            means.append(col_sum/rows)

    else:
        raise ValueError("Invalid mode given")

    return means
print(calculate_matrix_mean(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'))