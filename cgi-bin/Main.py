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
cgitb.enable(logdir="./logs.txt")
print ("Content-type:text/html\r\n\r\n")
'''Do form analysis here'''



form = cgi.FieldStorage()
value = form.getlist("Pos1")
pos = [float(i) for i in value]

value = form.getlist("Vel1")
vel = [float(i) for i in value]

value = form.getlist("Mass1")
mass = [float(i) for i in value]


current = 1
massData = [[[pos[i], pos[i + 1], pos[i + 2]],[vel[i], vel[i + 1], vel[i + 2]],mass[i]] for i in range(0,len(mass))]

print("<p>: ", massData)
'''
while(len(form.getlist("Pos" + str(current))) > 0):
    thisMass = []
    value = form.getlist("Pos" + str(current)))
    pos = [float(i) for i in value]
    value = form.getlist("Vel"+str(current)))
    vel = [float(i) for i in value]
    value = form.getlist("Vel"+str(current)))
    mass = [float(i) for i in value][0]
    current += 1
    massData.append([pos,vel,mass])
'''



''' Run the simulation '''



plt.figure(figsize = (8,6))
fig, ax = plt.subplots()


'''
Test what is currently going on

Global Variables
'''
timestep = 0.005
endTime = 1.5

masses = [pointMass('mass '+str(i),massData[i][0],massData[i][1], massData[i][2]) for i in range(0,len(massData))]
forces = [invSquareForce([4.0,4.0,0.0], -2)]
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
'''Each graph type has a separate draw method'''

def plotPositions():
    ''' Plot each mass separately '''

    for i in range(0, len(masses)):
        ax.plot([dataPoint[i][1][0] for dataPoint in data], [dataPoint[i][1][1] for dataPoint in data], label = data[0][i][0] , color = "C" + str(i))
    ax.plot([force.origin.toArray()[0] for force in forces if force.type == 'inverseSquare'], [force.origin.toArray()[1] for force in forces if force.type == 'inverseSquare'], "ko")
    ax.set_title("Trajectories")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.legend()

def plotEnergies():
    for i in range(0, len(masses)):
        ax.plot([0.5 * masses[i].mass * sum([component ** 2 for component in dataPoint[i][1]]) for dataPoint in data], [timestep * i for i in range(0,len(data))], label = data[0][i][0] , color = "C" + str(i))
        ax.set_title("Energies")
        ax.set_xlabel("Time")
        ax.set_ylabel("Energy")
    ax.legend()

def plotVelocities():
    ''' Plot each mass separately '''

    for i in range(0, len(masses)):
        ax.plot([dataPoint[i][2][0] for dataPoint in data], [dataPoint[i][2][1] for dataPoint in data], label = data[0][i][0] , color = "C" + str(i))
    ax.set_title("Velocities")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.legend()

''' Figure out what to graph based on form submission '''
if (len(form.getlist("GraphPosition.x")) > 0):
    plotPositions()
elif (len(form.getlist("KineticEnergy.x")) > 0):
    plotEnergies()
else:
    plotVelocities()
print(mpld3.fig_to_html(fig))
print("<a href = ..\\> Go Back </a>")
