#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:31 2024

@author: emanzaheer
"""

import openpyscad as ops

# Define the height and thickness of the letters
letter_height = 50
letter_thickness = 10

# Function to create the letter "E"
def create_E():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, letter_height // 2 - letter_thickness // 2, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, 0, 0])
    )

# Function to create the letter "M"
def create_M():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness, letter_thickness * 1.5, letter_thickness]).translate([letter_thickness, letter_height // 2, 0])
    )
def create_H():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness, letter_thickness, letter_thickness]).translate([letter_thickness, letter_height // 2, 0])
    )

# Function to create the letter "A"
def create_A():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height // 2, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0])
    )

# Function to create the letter "N"
def create_N():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, 25]).translate([letter_thickness+11, letter_thickness-10, 0])
    )

# Dictionary to map letters to their corresponding functions
letter_map = {
    'E': create_E,
    'M': create_M,
    'A': create_A,
    'N': create_N,
    'H': create_H
}

# Prompt the user to input a name (only letters E, M, A, N)
name_input = "HA"

# Create each letter with alternating colors and position them
x_offset = 0
letters = ops.Union()
colors = ['pink', 'green']

for i, letter in enumerate(name_input):
    if letter in letter_map:
        # Create the letter and color it alternately
        colored_letter = letter_map[letter]().color(colors[i % len(colors)])
        # Position the letter next to the previous one
        letters += colored_letter.translate([x_offset, 0, 0])
        # Update the offset for the next letter
        x_offset += letter_height

# Save the model to a .scad file
letters.write(f"{name_input}_letters.scad")
