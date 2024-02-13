import time
from tqdm import tqdm,trange
t1 = time.time()
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1, 0, 0],
     [0, 1, 0]]
A_plus_B = [[A[i][j] + B[i][j]
            for j in trange(len(A[0]))]
            for i in trange(len(A))]
t2 = time.time()
print(A_plus_B)
print(t2 - t1)
######################################
import numpy as np
import time
t1 = time.time()
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1, 0, 0],
     [0, 1, 0]]
t2 = time.time()
print(np.array(A) + np.array(B))
print(np.add(A, B))
print(t2 - t1)
