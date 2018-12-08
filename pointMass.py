#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:03:04 2018

@author: Pernille
"""

import math
import matplotlib.pyplot as plt

class pointMass:
    '''Class for point masses '''
    position = []
    velocity = []
    acceleration = [0,0]
    mass = 1.0
    nameTag = ''

    def __init__(self, name, position, velocity):
        self.position = position
        self.velocity = velocity
        self.nameTag = name
        #self.acceleration = acceleration
        print("Initiated a point mass at ",position," with velocity ", velocity)

    def broadcast(self):
        ''' Print out a debug message style dataline '''
        print(self.nameTag, " at", self.position," with velocity",self.velocity, "and mass ", self.mass)

    def visualiseData(self):
        '''return data in a nice format to graph'''
        return [self.nameTag, self.position, self.velocity]

    def updateMass(self, timeStep):
        ''' Update the particle's data after time timeStep '''
        print(len(self.acceleration))
        if len(self.velocity) >= len(self.position):
                    self.position = [float(self.position[i]) + float(self.velocity[i]) * timeStep for i in range(0,len(self.position))]
        if len(self.acceleration) >= len(self.velocity):
                    self.velocity = [float(self.velocity[i]) + float(self.acceleration[i]) * timeStep for i in range(0,len(self.acceleration))]

    def addForceContribution(self, force):
        ''' Update the mass acceleration due to a given force contribution '''
        self.acceleration = [self.acceleration[i] + force[i] / self.mass for i in range(0,len(self.acceleration))]
