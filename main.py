from random import randint
import numpy as np
import scipy as sp
import matplotlib.pyplot  as plt
import time
import keyboard

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

def returnAcceleration(pos, masses):
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
            a[i,0] += 6.67*10**(2) * relX * detR *  1 # note the +=. We are summing up the accels for each particle (N) rel to every other particle (N). so it comes to N**2
            a[i,1] += 6.67*10**(2) * relY * detR *  1
            a[i,2] += 6.67*10**(2) * relZ * detR *  1
    return a
    
pos = np.array(
    [
        [0,0,0],
        [10,0,0],
        # [5,5,0]
    ]
)
vel =  np.array(
    [
        [0,5,0],
        [0,-5,0],
        # [10,0,0]
    ]
)
masses = [1,1]
accel = returnAcceleration( pos, masses)
N = pos.shape[0]
step = 0.01
posHistory = [pos[0:N, 0:2].tolist()]
colors = ['red','green', 'blue', 'magenta', 'violet', 'orange', 'yellow', 'cyan']
tempPos = np.array(pos)
plot = plt.scatter(tempPos[::, 0], tempPos[::, 1],color=colors[0:N])
plt.pause(0.5)
for i in range(10000000):
    vel = vel +  accel*0.01/2
    pos = pos + vel*0.01
    accel = returnAcceleration(pos, masses)
    vel += accel*0.01/2
    posHistory.append(pos[0:N, 0:2].tolist())
    tempPos = np.array(pos)
    # print(tempPos)
    plot = plt.scatter(tempPos[::, 0], tempPos[::, 1],color=colors[0:N])
    if keyboard.is_pressed('c'):
        break
    plt.pause(0.01)
    #plot.remove()

posHistory = np.array(posHistory)
plt.show()