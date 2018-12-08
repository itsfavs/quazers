#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:03:04 2018

@author: Pernille
"""

import math

class pointMass:
    '''Class for point masses '''
    position = []
    velocity = []
    acceleration = []
    mass = 1.0

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        #self.acceleration = acceleration
        print("Initiated a point mass at ",position," with velocity ", velocity)

    def broadcast(self):
        print("point mass at", self.position," with velocity",self.velocity, "and mass ", self.mass)

    def update(self, timeStep):
        ''' Update the particle's data after time timeStep '''
        position = [float(self.position[i]) + self.velocity[i] * timeStep for i in range(0,len(self.position))]
