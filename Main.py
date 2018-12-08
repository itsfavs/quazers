from pointMass import pointMass
import matplotlib.pyplot as plt
import numpy
from Forces import constantForce

'''
Test what is currently going on
'''

'''
Global Variables
'''
timestep = 0.1
endTime = 5

masses = [pointMass('mass 1',[0,0],[1.0,0.0])]
forces = [constantForce([0,1.0])]
data = []

'''
Run a loop to update parameters
'''

def runSim():
    print("Beginning sim")
    time = 0
    while (time <= endTime):
        for mass in masses:
            for singleForce in forces:
                singleForce.updateForce(mass)
            mass.updateMass(timestep)
            mass.broadcast()
            data.append(mass.visualiseData())
        time += timestep

runSim()

plt.plot([i[1][0] for i in data], [i[1][1] for i in data])
