from random import randint
import numpy as np
import scipy as sp
import matplotlib.pyplot  as plt
import time
import keyboard

def returnAcceleration(pos, masses, currCount):
    #pos = N x 3
    #mass = N x 1
    softening = 0.1
    N = pos.shape[0]
    a = np.zeros((N,3)) # N x 3
    stop = False
    for i in range(N):
        for j in range(N):
            relX = pos[j,0] - pos[i,0]
            relY = pos[j,1] - pos[i,1]
            relZ = pos[j,2] - pos[i,2]
            detR = (relX**2 + relY**2 + relZ**2 + softening**0.2)**(-3/2)
            dis = (relX**2 + relY**2 + relZ**2)**0.5
            # the relX makes sure that the accel due to itself becomes 0
            a[i,0] += 6.67*10**(2) * relX * detR *  masses[j] # note the +=. We are summing up the accels for each particle (N) rel to every other particle (N). so it comes to N**2
            a[i,1] += 6.67*10**(2) * relY * detR *  masses[j]
            a[i,2] += 6.67*10**(2) * relZ * detR *  masses[j]
            if i!=j and dis<0.5 and currCount>25:
                stop = True
    return [a, stop]

# Position data ------
pos = np.array(
    [
        [0,0,0],
        [10,0,0],
        [20,0,0],
        [30,0,0],
        [29.9,0,0]
    ]
)
vel =  np.array(
    [
        [0,0,0],
        [0,100,0],
        [0,100,0],
        [0,100,0],
        [-200,100,0]
    ]
)
masses = [1000,1,2,3,0.0001]
step = 0.0001
#------------------------

def nBodySimulator(pos, vel, masses, step):

    colors = ['red','green', 'blue', 'magenta', 'violet', 'orange', 'yellow', 'cyan']
    N = pos.shape[0]

    # Initial accelerations
    [accel,stop] = returnAcceleration( pos, masses, 0)
    posHistory = [pos[0:N, 0:2].tolist()]
    tempPos = np.array(pos)
    plot = plt.scatter(tempPos[::, 0], tempPos[::, 1],color=colors[0:N])
    plt.pause(0.5)

    for i in range(100000000000000):
        # break
        vel = vel +  accel*step/2
        pos = pos + vel*step
        [accel,stop] = returnAcceleration(pos, masses,i)
        vel += accel*step/2
        posHistory.append(pos[0:N, 0:2].tolist())
        tempPos = np.array(pos)
        plot = plt.scatter(tempPos[::, 0], tempPos[::, 1],color=colors[0:N])
        if keyboard.is_pressed('c') or stop==True:
            break
        plt.pause(0.01)
        #plot.remove()

    posHistory = np.array(posHistory)
    plt.show()

# ---- Function Call
nBodySimulator(pos, vel, masses, step)