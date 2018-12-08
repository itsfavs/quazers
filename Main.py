from pointMass import pointMass

'''
Test what is currently going on
'''

'''
Global Variables
'''
timestep = 0.1
endTime = 5

masses = [pointMass([0,0],[1.0,2.0])]

'''
Run a loop to update parameters
'''

def runSim():
    print("Beginning sim")
    time = 0
    while (time <= endTime):
        for mass in masses:
            mass.update(timestep)
            mass.broadcast()
        time += timestep

runSim()
