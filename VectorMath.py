import math

class vector:
    '''Class to work with vectors'''
    components = []

    def __init__(self,components):
        self.components = components

    def magnitudeSquared(self):
        return sum([i ** 2 for i in self.components])

    def magnitude(self):
        return self.magnitudeSquared() ** 0.5

    def normalise(self):
        return vector([component * (1 / self.magnitude()) for component in self.components])

    def __str__(self):
        return str([self.components[i] for i in range(0, len(self.components))])
    def __len__(self):
        return len(self.components)
    def toArray(self):
        return [self.components[i] for i in range(0, len(self.components))]

    ''' Vector operations'''

    def dot(self, other):
        return sum([self.components[i] * other.components[i] for i in range(0, len(self.components))])

    def __add__(self, other):
        return vector([self.components[i] + other.components[i] for i in range(0, len(self.components))])

    def __sub__(self, other):
        return vector([self.components[i] - other.components[i] for i in range(0, len(self.components))])
    '''multiply by a scalar'''
    def __mul__(self, other):
        return vector([component * other for component in self.components])
    def __rmul__(self, other):
        return vector([self.components[i] * other for i in range(0, len(self.components))])

    def __truediv__(self, other):
        return self * (1 / other)
    def __rtruediv__(self, other):
        return self * (1 / other)
