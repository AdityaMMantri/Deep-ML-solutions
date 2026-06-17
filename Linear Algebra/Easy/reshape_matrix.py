import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    new_row,new_col=new_shape
    old_row=len(a)
    old_col=len(a[0])

    if old_row*old_col!=new_row*new_col:
        return []
    
    flatten_matrix=[]

    for row in a:
        for value in row:
            flatten_matrix.append(value)
    
    result = []
    idx=0

    for i in range(new_row):
        row=[]
        for j in range(new_col):
            row.append(flatten_matrix[idx])
            idx+=1
        result.append(row)
    return result
a = [[1, 2],
     [3, 4],
     [5, 6],
     [7, 8]]

print(reshape_matrix(a, (2, 4)))