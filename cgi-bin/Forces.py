import math
from VectorMath import vector

class force:
    ''' General force class to use for inhritance '''
    type = ''
    updateForce = None


class constantForce (force):
    ''' constant force '''

    type = 'constant'
    direction = None

    def __init__(self, direction):
        self.direction = vector(direction)

    def updateForce(self, object):
        object.addForceContribution(self.direction)


class invSquareForce (force):
    ''' Inverse square forcefield '''

    type = 'inverseSquare'
    origin = None
    constant = 1.0

    def __init__(self, origin, constant):
        self.origin = vector(origin)
        self.constant = constant

    def updateForce(self, object):
        ''' Calculate displacement vector and normed displacement'''
        displacement = object.position - self.origin
        ''' Normed displacement is calculated by dividing each component of
        displacement by the magnitude of the displacement vector '''
        normedDisplacement = displacement / displacement.magnitude()

        result = normedDisplacement * self.constant / displacement.magnitudeSquared()
        object.addForceContribution(result)

class linearForce (force):
    ''' Forcefield dependent linearly on position (Hooke's law) '''
    type = 'linear'
    origin = None
    constant = 1.0

    def __init__(self, origin, constant):
        self.origin = vector(origin)
        self.constant = constant

    def updateForce(self, object):
        displacement = object.position - self.origin
        result = displacement * self.constant
        object.addForceContribution(result)

class gravForce (force):
    ''' General force used to define the force between two masses '''

    type = 'grav'
    origin = None
    constant = 1.0

    def __init__(self,  origin, constant):
        self.origin = vector(origin)
        self.constant = constant

    def updateForce(self, object):
        ''' Calculate displacement vector and normed displacement'''
        displacement = object.position - self.origin
        ''' Normed displacement is calculated by dividing each component of
        displacement by the magnitude of the displacement vector '''
        normedDisplacement = displacement / displacement.magnitude()

        result = normedDisplacement * self.constant * object.mass / displacement.magnitudeSquared()
        object.addForceContribution(result)
