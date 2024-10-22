#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:31 2024

@author: emanzaheer
"""

import openpyscad as ops

# largest cube
cubes = ops.Cube([100, 100, 100])

# Variables for initial position
x, y, z = 0, 0, 100

# Create progressively smaller cubes from size 99 to 1
for size in range(99, 0, -1):
    # Create the next cube and translate it on top of the previous one
    cubes += ops.Cube([size, size, size]).translate([x, y, z])
    # Update the z position for the next cube to stack on top
    z += size

# Save the model to a .scad file
cubes.write("progressive_cubes.scad")
