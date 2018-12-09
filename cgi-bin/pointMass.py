#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:03:04 2018

@author: Pernille
"""

import math
import matplotlib.pyplot as plt
from VectorMath import vector

class pointMass:
    '''Class for point masses '''
    position = None
    velocity = None
    acceleration = vector([0,0])
    mass = 1.0
    nameTag = ''
    attachedField = None

    def __init__(self, name, position, velocity, attachedField = None):
        self.position = vector(position)
        self.velocity = vector(velocity)
        self.acceleration = vector([0 for i in range(0,len(position))])
        self.nameTag = name
        self.attachedField = attachedField
        #self.acceleration = acceleration
        print("Initiated a point mass at ",position," with velocity ", velocity)

    def broadcast(self):
        ''' Print out a debug message style dataline '''
        print(self.nameTag, " at", self.position," with velocity",self.velocity, "and mass ", self.mass)

    def visualiseData(self):
        '''return data in a nice format to graph'''
        return [self.nameTag, self.position.toArray(), self.velocity.toArray()]

    def updateMass(self, timeStep):
        ''' Update the particle's data after time timeStep '''
        if len(self.velocity) >= len(self.position):
                    self.position = self.position + (self.velocity * timeStep)
        if len(self.acceleration) >= len(self.velocity):
                    self.velocity = self.velocity + self.acceleration * timeStep

    def addForceContribution(self, force):
        ''' Update the mass acceleration due to a given force contribution '''
        self.acceleration = self.acceleration + force * (1.0 / self.mass)
