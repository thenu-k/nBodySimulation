import numpy as np
import scipy as sp
import matplotlib  as plt

# x = np.array(
#     [[1,2],
#     [3,4],
#     [5,6]]
# )
# x1 = x[:, 0:1]
# x2 = x1.T
# print(x1, x2)
# # This is called broadcasting. It is not normal vector substraction
# print(x2 - x1)

def returnAcceleration(pos, mass):
    #pos = N x 3
    #mas = N x 1
    N = pos.shape[0]
    a = np.zeros((N,3))
    relXAll = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            relX = pos[j,0] - pos[i,0]
            relXAll[j,i]  = relX
    print(relXAll)

pos = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
returnAcceleration(pos, 1)