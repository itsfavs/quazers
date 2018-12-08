import numpy

class force:
    ''' General force class to use for inhritance '''
    type = ''
    updateForce = None


class constantForce (force):
    ''' Inverse square forcefield '''

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
