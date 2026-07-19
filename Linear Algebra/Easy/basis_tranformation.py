import numpy as np
B = [[1, 0, 0], 
     [0, 1, 0], 
     [0, 0, 1]]
C = [[1, 2.3, 3], 
     [4.4, 25, 6], 
     [7.4, 8, 9]]

C_inv=np.linalg.inv(C)
P=C_inv @ B
print(P)