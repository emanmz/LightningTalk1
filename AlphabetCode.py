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
space_width = letter_height // 2  # Define how wide a space should be

# Function to create the letter "A"
def create_A():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height // 2, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0])
    )

# Function to create the letter "B"
def create_B():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, letter_height // 2 - letter_thickness // 2, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, 0, 0])+
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([letter_thickness*2,0,0])-
        ops.Cube([letter_thickness *1.5, letter_thickness, letter_thickness*1.5]).translate([letter_thickness*2,letter_thickness*2, -0.5])
    )

# Function to create the letter "C"
def create_C():
    return (
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]) +
        ops.Cube([letter_thickness, letter_height - (letter_thickness * 2), letter_thickness]).translate([0, letter_thickness, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0])
        )

# Function to create the letter "D"
def create_D():
    return (
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]) +
        ops.Cube([letter_thickness, letter_height - (letter_thickness * 2), letter_thickness]).translate([0, letter_thickness, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0])+
        ops.Cube([letter_thickness, letter_height - (letter_thickness * 2), letter_thickness]).translate([letter_thickness*3, letter_thickness, 0])
    )

# Function to create the letter "E"
def create_E():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, letter_height // 2 - letter_thickness // 2, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, 0, 0])
    )

# Function to create the letter "F"
def create_F():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, letter_height // 2 - letter_thickness // 2, 0])
    )

# Function to create the letter "G"
def create_G():
    return (
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]) +
        ops.Cube([letter_thickness, letter_height - (letter_thickness * 2), letter_thickness]).translate([0, letter_thickness, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0])+
        ops.Cube([letter_thickness, letter_height - (letter_thickness * 3), letter_thickness]).translate([letter_thickness*3, 0, 0])

    )

# Function to create the letter "H"
def create_H():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness, letter_thickness, letter_thickness]).translate([letter_thickness, letter_height // 2, 0])
    )

# Function to create the letter "I"
def create_I():
    vertical_thickness = letter_thickness  # Thickness of the vertical line
    vertical_height = letter_height          # Height of the vertical line
    horizontal_thickness = letter_thickness   # Thickness of the horizontal lines
    horizontal_length = vertical_thickness * 3  # Length of the horizontal lines

    return (
        ops.Cube([vertical_thickness, vertical_height, vertical_thickness]).translate([vertical_thickness, 0, 0]) +  # Vertical line
        ops.Cube([horizontal_length, horizontal_thickness, horizontal_thickness]).translate([0, vertical_height - horizontal_thickness, 0]) +  # Top horizontal line
        ops.Cube([horizontal_length, horizontal_thickness, horizontal_thickness]).translate([0, 0, 0])  # Bottom horizontal line
    )

# Function to create the letter "J"
def create_J():
    return (
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness, letter_height - letter_thickness, letter_thickness]).translate([letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, 0, 0])
    )

# Function to create the letter "K"
# Function to create the letter "K"
def create_K():
    vertical_thickness = letter_thickness     # Thickness of the vertical line
    vertical_height = letter_height            # Height of the vertical line
    diagonal_thickness = letter_thickness      # Thickness of the diagonal lines
    diagonal_length = vertical_height / 1.5    # Length of the diagonal lines

    return (
        ops.Cube([vertical_thickness, vertical_height, vertical_thickness]) +  # Vertical line
        ops.Cube([diagonal_thickness, diagonal_length, diagonal_thickness]).rotate([0, 0, -45]).translate([0, vertical_height / 2, 0]) +  # Upper diagonal line
        ops.Cube([diagonal_thickness, diagonal_length, diagonal_thickness]).rotate([0, 0, -135]).translate([letter_thickness, vertical_height / 2, 0])  # Lower diagonal line
    )


# Function to create the letter "L"
def create_L():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, 0, 0])
    )

# Function to create the letter "M"
def create_M():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness, letter_thickness * 1.5, letter_thickness]).translate([letter_thickness, letter_height // 2, 0])
    )

# Function to create the letter "N"
def create_N():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) + 
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, 25]).translate([letter_thickness + 11, letter_thickness - 10, 0])
    )

# Function to create the letter "O"
def create_O():
    outer_radius = letter_thickness * 2  # Increased outer radius for a larger circle
    inner_radius = letter_thickness      # Inner radius based on letter thickness
    
    # Create the outer circle
    outer_circle = ops.Cylinder(h=letter_thickness, r=outer_radius, segments=64)

    # Create the inner cut-out circle
    inner_circle = ops.Cylinder(h=letter_thickness + 1, r=inner_radius, segments=64).translate([0, 0, -0.5])

    # Combine the shapes and move everything up on the Y-axis only
    q_shape = outer_circle - inner_circle
    return q_shape.translate([letter_thickness, (letter_height / 1.25) - outer_radius, 0])


# Function to create the letter "P"
def create_P():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) +
        ops.Cube([letter_thickness * 2, letter_thickness * 2, letter_thickness]).translate([letter_thickness, letter_height - letter_thickness * 2, 0])
    )

# Function to create the letter "Q"
def create_Q():
    outer_radius = letter_thickness * 2  # Increased outer radius for a larger circle
    inner_radius = letter_thickness      # Inner radius based on letter thickness
    tail_thickness = letter_thickness / 2  # Thinner tail to look more proportional
    tail_length = letter_thickness * 1.5   # Length of the tail to look like a proper Q

    # Create the outer circle
    outer_circle = ops.Cylinder(h=letter_thickness, r=outer_radius, segments=64)

    # Create the inner cut-out circle
    inner_circle = ops.Cylinder(h=letter_thickness + 1, r=inner_radius, segments=64).translate([0, 0, -0.5])

    # Create the tail for the "Q" and position it at the bottom-right
    tail = ops.Cube([tail_thickness, tail_length, letter_thickness]).rotate([0, 0, 45]).translate([outer_radius - tail_thickness, -outer_radius, 0])

    # Combine the shapes and move everything up on the Y-axis only
    q_shape = outer_circle - inner_circle + tail
    return q_shape.translate([letter_thickness, (letter_height / 1.25) - outer_radius, 0])


# Function to create the letter "R"
def create_R():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]) +
        ops.Cube([letter_thickness * 2, letter_thickness * 2, letter_thickness]).translate([letter_thickness, letter_height - letter_thickness * 2, 0]) +
        ops.Cube([letter_thickness, letter_height/1.5, letter_thickness]).rotate([0, 0, -150]).translate([letter_thickness, letter_height/1.5, 0])  # Lower diagonal line
    )

# Function to create the letter "S"
def create_S():
    return(
        ops.Cube([letter_thickness, letter_height/1.7, letter_thickness]).translate([letter_thickness*2, 0, 0]) + 
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, letter_height // 2 - letter_thickness // 2, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, 0, 0])+
        ops.Cube([letter_thickness, letter_height/2, letter_thickness]).translate([0, letter_height/2, 0])
        )



# Function to create the letter "T"
def create_T():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]).translate([letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0])
    )

# Function to create the letter "U"
def create_U():
    return (
        ops.Cube([letter_thickness, letter_height - letter_thickness, letter_thickness]) +
        ops.Cube([letter_thickness, letter_height - letter_thickness, letter_thickness]).translate([2 * letter_thickness, 0, 0]) +
        ops.Cube([letter_thickness * 2, letter_thickness, letter_thickness]).translate([0, 0, 0])
    )

# Function to create the letter "V"
def create_V():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, 15]).translate([0, 0, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, -15]).translate([0, 0, 0])
    )

# Function to create the letter "W"
def create_W():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, 15]).translate([0, 0, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, -15]).translate([0, 0, 0])+
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, 15]).translate([letter_thickness*2,0,0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, -15]).translate([letter_thickness*2,0,0])
)
# Function to create the letter "X"
def create_X():
    return (
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, 25]).translate([letter_thickness*3, 0, 0]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, -25]).translate([letter_thickness, 0, 0])
    )

# Function to create the letter "Y"
def create_Y():
    return (
        ops.Cube([letter_thickness, letter_height/2, letter_thickness]).rotate([0, 0, 25]).translate([letter_thickness*2, letter_height/2, 0])+
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0, 0, -25]).translate([letter_thickness, 0, 0])
    )

# Function to create the letter "Z"
def create_Z():
    return (
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]) +
        ops.Cube([letter_thickness, letter_height, letter_thickness]).rotate([0,0,-25]).translate([0, letter_thickness/2, 0]) +
        ops.Cube([letter_thickness * 3, letter_thickness, letter_thickness]).translate([0, letter_height - letter_thickness, 0])
    )

# Function to create the exclamation point "!"
def create_exclamation():
    # Main vertical bar
    bar = ops.Cube([letter_thickness, letter_height, letter_thickness])
    # Dot
    dot = ops.Cube([letter_thickness, letter_thickness, letter_thickness]).translate([0, -letter_thickness * 2, 0])
    full_exla = bar + dot
    return full_exla.translate([0,letter_thickness*2,0])

# Dictionary to map letters to their corresponding functions
letter_map = {
    'A': create_A,
    'B': create_B,
    'C': create_C,
    'D': create_D,
    'E': create_E,
    'F': create_F,
    'G': create_G,
    'H': create_H,
    'I': create_I,
    'J': create_J,
    'K': create_K,
    'L': create_L,
    'M': create_M,
    'N': create_N,
    'O': create_O,
    'P': create_P,
    'Q': create_Q,
    'R': create_R,
    'S': create_S,
    'T': create_T,
    'U': create_U,
    'V': create_V,
    'W': create_W,
    'X': create_X,
    'Y': create_Y,
    'Z': create_Z,
    '!': create_exclamation
}

# Function to create any letter or supported symbol
def create_character(char):
    if char in letter_map:
        return letter_map[char]()
    else:
        raise ValueError(f"Character '{char}' not supported.")

# Input field for the text
name_input = input("Enter your text (use only the supported characters A-Z and '!'): ").strip().upper()

# Input field for the colors, separated by commas
color_input = input("Enter colors for the letters (separate by commas): ").strip()
colors = [color.strip() for color in color_input.split(',')]

# Space width for spacing between letters
space_width = letter_height  # You can adjust this value as needed

# Create each letter with alternating colors and position them
x_offset = 0
letters = ops.Union()

for i, letter in enumerate(name_input):
    if letter == ' ':
        # If the letter is a space, increase x_offset by the space width and skip
        x_offset += space_width
        continue
    if letter in letter_map:
        # Create the letter and color it with user-defined colors
        colored_letter = letter_map[letter]().color(colors[i % len(colors)])
        # Position the letter next to the previous one
        letters += colored_letter.translate([x_offset, 0, 0])
        # Update the offset for the next letter
        x_offset += letter_height

# Save the model to a .scad file
letters.write(f"{name_input}_letters.scad")
