#!C:\Program Files (x86)\Python37-32\python.exe -u
from pointMass import pointMass
import matplotlib.pyplot as plt
import mpld3
import Forces
from Forces import linearForce
from Forces import invSquareForce
from VectorMath import vector

import cgi
import cgitb
cgitb.enable()
print ("Content-type:text/html\r\n\r\n")
'''Do form analysis here'''

form = cgi.FieldStorage()
value = form.getlist("Pos1")
pos1 = [float(i) for i in value]
print("<p>Position:", pos1)

value = form.getlist("Vel1")
vel1 = [float(i) for i in value]
print("<p>Velocity:", vel1)

pos1 = [pos1[0],pos1[1]]
vel1 = [vel1[0],vel1[1]]

''' Run the simulation '''



plt.figure(figsize = (8,6))
fig, ax = plt.subplots()

'''
Test what is currently going on

Global Variables
'''
timestep = 0.005
endTime = 1.5

masses = [pointMass('mass 1',pos1,vel1)]
forces = [invSquareForce([4.0,4.0], -2)]
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
        ax.plot([dataPoint[i][1][0] for dataPoint in data], [dataPoint[i][1][1] for dataPoint in data], label = data[0][i][0] , color = "C" + str(i))

    ax.plot([force.origin.toArray()[0] for force in forces if force.type == 'inverseSquare'], [force.origin.toArray()[1] for force in forces if force.type == 'inverseSquare'], "ko")
    ax.legend()
plotPositions()
html = mpld3.fig_to_html(fig)
print(html)
print("<a href = ..\\> Go Back </a>")
