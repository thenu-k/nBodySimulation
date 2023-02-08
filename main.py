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
    #mass = N x 1
    softening = 0.1
    N = pos.shape[0]
    a = np.zeros((N,3)) # N x 3
    for i in range(N):
        for j in range(N):
            relX = pos[j,0] - pos[i,0]
            relY = pos[j,1] - pos[i,1]
            relZ = pos[j,2] - pos[i,2]
            detR = (relX**2 + relY**2 + relZ**2 + softening**0.2)**(-3/2)
            a[i,0] += 6.67*10**(2) * relX * detR *  mass # note the +=. We are summing up the accels for each particle (N) rel to every other particle (N). so it comes to N**2
            a[i,1] += 6.67*10**(2) * relY * detR *  mass
            a[i,2] += 6.67*10**(2) * relZ * detR *  mass
    return a
    
pos = np.array(
    [
        [1,2,0],
        [4,5,0],
        # [7,8,0]
    ]
)
vel =  np.array(
    [
        [1,2,0],
        [4,5,0],
        # [7,8,0]
    ]
)
mass = 100
accel = returnAcceleration( pos, mass)
for i in range(10):
    vel = vel +  accel*0.01/2
    pos = pos + vel*0.01
    accel = returnAcceleration(pos, mass)
    vel += accel*0.01/2
    print('.....')
    dis = pos[0,0:pos.shape[1]] - pos[1,0:pos.shape[1]]
    # print((dis[0]**2 + dis[1]**2)**0.5)
    print(pos)
