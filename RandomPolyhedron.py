#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:31 2024

@author: emanzaheer
"""

import openpyscad as ops
import random

def random_point():
    return [
        random.uniform(-200, 200),  # x coordinate
        random.uniform(-200, 200),  # y coordinate
        random.uniform(-200, 200)   # z coordinate
    ]

def random_polyhedron():
    points = [random_point() for _ in range(5)]
    faces = [
        [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4],  [1, 0, 3], [2, 1, 3]]
    
    return ops.Polyhedron(points=points, faces=faces)

# Generate and save the polyhedron
p = random_polyhedron()
p.write("Random_Polyhedron.scad")
