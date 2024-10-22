import openpyscad as ops

# # Step 1: Basic shapes

# cube1 = ops.Cube([10, 20, 10])
# cube1.write("demo_output.scad")
# cube2 = ops.Cube([20, 10, 10])
# cube2.write("demo_output.scad")
# sphere1 = ops.Sphere(r=10, _fn=100)
# sphere1.write("demo_output.scad")

# # Step 2: Boolean operations

# union_example = cube1 + cube2   # Union of two cubes
# union_example.write("demo_output.scad")
# difference_example = cube1 - sphere1  # Difference of two cubes
# difference_example.write("demo_output.scad")
# intersection_example = cube1 & cube2  # Intersection of two cubes
# intersection_example.write("demo_output.scad")

# # Step 3: Transformations

# translated_cube = cube1.translate([10, 10, 10])  # Moving a cube in space
# translated_cube.write("demo_output.scad")
# rotated_cube = cube2.rotate([0, 0, 45])  # Rotating a cube by 45 degrees
# rotated_cube.write("demo_output.scad")
# scaled_cube = cube2.scale([2, 1, 1])  # Scaling a cube differently in x, y, z directions
# scaled_cube.write("demo_output.scad")

# # Step 4: Complex shape combination with transformations

# complex_shape = (sphere1 + rotated_cube).translate([10, 0, 0])
# complex_shape.write("demo_output.scad")

# # Step 5: Color and Offset example

# colored_cube = cube1.color("#CC5500")  # Applying a color to a cube
# colored_cube.write("demo_output.scad")

# offset_circle = ops.Circle(10).offset(5)  # Creating a circle with an offset
# offset_circle.write("demo_output.scad")

# # Write the result to an SCAD file to be visualized in OpenSCAD
# (complex_shape + union_example + translated_cube + colored_cube).write("demo_output.scad")