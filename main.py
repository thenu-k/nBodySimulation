from random import randint
import numpy as np
import scipy as sp
import matplotlib.pyplot  as plt
from matplotlib.animation import FuncAnimation
import time
import keyboard

def returnAcceleration(pos,vel, masses, detectCollisionsOf):
    #pos = N x 3
    #mass = N x 1
    softening = 0.1
    N = pos.shape[0]
    a = np.zeros((N,3)) # N x 3
    stop = False
    energy = 0
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
            # detecting any specified collisons
            if (set([i,j])==set(detectCollisionsOf)) and dis<0.1:
                stop = True
            # checking the total energy
            if i!=j:
                energy += -(6.67*10**(2) * masses[i] * masses[j])
        detV = (vel[i,0]**2 + vel[i,1]**2 + vel[i,2]**2)**0.5
        energy += 0.5*masses[i]*(detV**2)
    return [a, stop, energy]

# Position data ------
pos = np.array(
    [
        [0,0,0],
        [10,0,0],
        [20,0,0],
        [30,0,0]
    ]
)
vel =  np.array(
    [
        [0,0,0],
        [0,100,0],
        [0,100,0],
        [0,100,0]
    ]
)
masses = [1000,1,2,3]
step = 0.001

numParticles = 30
pos2 = np.random.rand(numParticles,3)
vel2 = np.random.rand(numParticles,3)
masses2 = np.random.rand(numParticles)
#------------------------

def nBodySimulator(pos, vel, masses, step, detectCollisionsOf, displayEnergy, numSteps, dimensions, displayTrails):

    plotHistory = []

    colors = []
    for i in range(200):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    N = pos.shape[0]

    # Initial accelerations
    [accel,stop, energy] = returnAcceleration( pos,vel, masses, detectCollisionsOf)
    #print(energy)
    posHistory = [pos[0:N, 0:3].tolist()]
    energyHistory = [energy]
    tempPos = np.array(pos)

    for i in range(numSteps):
        # completion %
        currentPercentage = (i/numSteps)*100
        print('Completion: '+ "{:.2f}".format(currentPercentage) + ' %', end='\r')
        # break
        vel = vel +  accel*step/2
        pos = pos + vel*step
        [accel,stop, energy] = returnAcceleration(pos,vel, masses, detectCollisionsOf)
        #print(energy)
        vel += accel*step/2
        posHistory.append(pos[0:N, 0:3].tolist())
        energyHistory.append(energy)
        tempPos = np.array(pos)
        if keyboard.is_pressed('c') or stop==True:
            break

    posHistory = np.array(posHistory)
    # print(energyHistory)


    fig = plt.figure()
    if dimensions == 3:
        ax = plt.axes(projection='3d')
    if dimensions == 2:
        ax = plt.axes()
    def animate(count):
        currentXValues =  posHistory[count,0:N,0]
        currentYValues =  posHistory[count,0:N,1]
        currentZValues =  posHistory[count,0:N,2]
        if displayTrails==False: 
            ax.clear()
        if dimensions == 3:
            ax.scatter(currentXValues, currentYValues,currentZValues, color=colors[0:N])
        if dimensions ==2: 
            ax.scatter(currentXValues, currentYValues, color=colors[0:N])
    ani = FuncAnimation(fig, animate, frames=numSteps, interval=5, repeat=False)
    plt.show()


# ---- Function Call
dimensions = 3
numSteps = 3000
displayTrails = False
nBodySimulator(pos2, vel2, masses2, step, [3,7000], False, numSteps, dimensions, displayTrails)