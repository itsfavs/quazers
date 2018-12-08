#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:03:04 2018

@author: Pernille
"""

import math
import numpy

class pointMass:
    '''Class for point masses '''
    position = []
    velocity = []
    mass = 1
    
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
        