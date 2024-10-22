import openpyscad as ops

def menger_sponge(size, level):
    if level == 0:
        return ops.Cube([size, size, size])
    new_size = size / 3
    sponge_parts = []
    # sub-cubes by skipping the central cube of each 3x3 grid
    
    for x in range(3):
        for y in range(3):
            for z in range(3):
                # Skip the center cubes (1,1,1) in each dimension to create the hollow Menger Sponge pattern
                if (x == 1 and y == 1) or (x == 1 and z == 1) or (y == 1 and z == 1):
                    continue
                # Recursively create smaller sub-cubes
                part = menger_sponge(new_size, level - 1).translate([x * new_size, y * new_size, z * new_size])
                sponge_parts.append(part)
    # Sum all the parts to create a union of cubes
    sponge_union = sponge_parts[0]
    for part in sponge_parts[1:]:
        sponge_union += part
    return sponge_union

# going over level 3 DOES NOT LOAD. it is WAYYYY to many cubes
size = 30
level = 0
# Generate the Menger Sponge
sponge = menger_sponge(size, level)
# Optional: Apply transformations and color
colored_sponge = sponge.color("#CC5500").rotate([0, 0, 45])
# Save the result to a SCAD file
colored_sponge.write(f"{size}_{level}_menger_sponge.scad")