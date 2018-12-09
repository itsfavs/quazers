#!C:\Program Files (x86)\Python37-32\python.exe -u
from pointMass import pointMass
import matplotlib.pyplot as plt
import mpld3
import Forces
from Forces import linearForce
from VectorMath import vector

import cgi
import cgitb
cgitb.enable()
print ("Content-type:text/html\r\n\r\n")
print("<p> sfvfdbjyjrtshtrdjytjtnd </p>")

plt.figure(figsize = (8,6))

'''
Test what is currently going on

Global Variables
'''
timestep = 0.005
endTime = 1.5

masses = [pointMass('mass 1',[0,0],[2,0.0]), pointMass('mass 2',[0,0],[1,0.0])]
forces = [linearForce([4.0,4.0], -2)]
data = []

'''
Run a loop to update parameters
'''

def runSim():
    #print("Beginning sim")
    time = 0
    while (time <= endTime):
        currentData = []
        for mass in masses:
            for singleForce in forces:
                singleForce.updateForce(mass)
            mass.updateMass(timestep)
            currentData.append(mass.visualiseData())
        time += timestep
        data.append(currentData)

runSim()

def plotPositions():
    ''' Plot each mass separately '''
    for i in range(0, len(masses)):
        plt.plot([dataPoint[i][1][0] for dataPoint in data], [dataPoint[i][1][1] for dataPoint in data], label = data[0][i][0] , color = "C" + str(i))

    plt.plot([force.origin.toArray()[0] for force in forces if force.type == 'inverseSquare'], [force.origin.toArray()[1] for force in forces if force.type == 'inverseSquare'], "ko")
    plt.legend()
plotPositions()
html = mpld3.fig_to_html()
print html
