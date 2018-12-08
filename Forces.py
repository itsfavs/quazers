import numpy
import math

class force:
    ''' General force class to use for inhritance '''
    type = ''
    updateForce = None


class constantForce (force):
    ''' constant force '''

    type = 'constant'
    direction = []

    def __init__(self, direction):
        self.direction = direction

    def updateForce(self, object):
        object.addForceContribution(self.direction)


class invSquareForce (force):
    ''' Inverse square forcefield '''

    type = 'inverseSquare'
    origin = []
    constant = 1.0

    def __init__(self, origin, constant):
        self.origin = origin
        self.constant = constant

    def updateForce(self, object):
        ''' Calculate displacement vector and normed displacement'''
        displacement = [object.position[i] - self.origin[i] for i in range(0,len(self.origin))]
        ''' Normed displacement is calculated by dividing each component of
        displacement by the magnitude of the displacement vector '''
        normedDisplacement = [float(component) / sum([i ** 2 for i in displacement]) ** 0.5 for component in displacement]

        result = [self.constant * component / sum([i ** 2 for i in displacement]) for component in normedDisplacement ]
        object.addForceContribution(result)

class hookesLaw (force):
    ''' General force used for mass spring system'''

    type = ''
    origin = []
    constant = 1.0

    def __init__(self, origin, constant):
        self.origin = origin
        self.constant = constant

        def updateForce(self, object):
            ''' Multiply constant by displacement '''
            displacement = [object,position[i - self.origin[i] for i in range(0,len(self.origin))]
            ''' Displacement is calculated by dividing the
            displacement vector by its magnitude '''
            Displacement = [float(component) / sum([i ** 2 for i in displacement]) ** 0.5 for component in displacement]

            result = [self.constant * component / sum([i ** 2 for i in displacement]) for component in normedDisplacement ]
            object.addForceContribution(result)

class gravForce ():
    ''' General force used to define the force between two masses '''

    type = 'inverse square'
    origin = []
    constant = 1.0

    def __inti__(self,  origin, constant):
        self.origin = origin
        self.constant = constant

        def updateForce(self, object):
            ''' Calculate displacement vector and normed displacement'''
            displacement = [object.position[i] - self.origin[i] for i in range(0,len(self.origin))]
            ''' Normed displacement is calculated by dividing each component of
            displacement by the magnitude of the displacement vector '''
            normedDisplacement = [float(component) / sum([i ** 2 for i in displacement]) ** 0.5 for component in displacement]

            result = [object.mass * self.constant * component / sum([i ** 2 for i in displacement]) for component in normedDisplacement ]
            object.addForceContribution(result)
