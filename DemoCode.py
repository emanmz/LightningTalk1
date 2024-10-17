import openpyscad as ops


c1 = ops.Cube([10, 20, 10])
c2 = ops.Cube([20, 10, 10])
(c1 + c2).write("sample.scad")

p = ops.Polyhedron(
    points=[
        [10, 10, 0], [10, -10, 0], [-10, -10, 0], [-10, 10, 0],  [0, 0, 10]
    ],
    faces=[
        [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4],  [1, 0, 3], [2, 1, 3]
    ]
)

p.write("test2.scad")