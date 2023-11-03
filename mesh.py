import numpy as np

def generate_heightmap(map_size):
    seed = int(random.random()*1000)
    minimum = 0
    maximum = 0
    heightmap = np.zeros(map_size)

    for x in range(map_size[0]):
        for y in range(map_size[1]):
            new_value = update_point((x, y), seed)
            heightmap[x][y] = new_value
    return normalize(heightmap)
def expo(heightmap, heightmap_size, e):
    for x in range(heightmap_size[0]):
        for y in range(heightmap_size[1]):
            heightmap[x][y] = heightmap[x][y]**e
    return normalize(heightmap)

lut_vectors = (
    (-1, 1), (0, 1), (1, 1),
    (-1, 0),         (1, 0),
    (-1, -1), (0, -1), (1, -1)
)

def generate_slopemap(heightmap, heightmap_size):
    slopemap = np.zeros(heightmap_size)
    for x in range(heightmap_size[0]):
        for y in range(heightmap_size[1]):
            slope = 0
            for vector in lut_vectors:
                coord = (x+vector[0], y+vector[1])
                if out_of_bounds(coord):
                    continue
                slope += abs(heightmap[x][y]-heightmap[coord[0]][coord[1]])
            slope = slope/8
            slopemap[x][y] = slope
    return normalize(slopemap)

def get_color(height, slope):
    if height > 0.2 and height < 0.9 and slope > 0.45:
        return COLORS["rock"]
    if height <= 0.2:
        return COLORS["water"]
    elif height > 0.2 and height <= 0.225:
        return COLORS["sand"]
    elif height > 0.225 and height <= 0.45:
        return COLORS["grass"]
    elif height > 0.45 and height <= 0.85:
        return COLORS["forest"]
    elif height > 0.85 and height <= 0.9:
        return COLORS["rock"]
    elif height > 0.9:
        return COLORS["snow"]

vertices = [(x1, y1, z1), (x2, y2, z2), ... , (xn, yn, zn)]
tris = [(0, 1, 2), (0, 2, 3), ...]

new_index = original_x_size * x + y

def generate_vertices(heightmap, heightmap_size):
    vertices = []

    # The origin and size of mesh
    origin = (-1, -0.75, -1)
    size = 2
    max_height = 0.5

    # We need to calculate the step between vertices 
    step_x = size/(heightmap_size[0]-1)
    step_y = size/(heightmap_size[1]-1)

    for x in range(heightmap_size[0]):
        for y in range(heightmap_size[1]):
            x_coord = base[0] + step_x*x 
            y_coord = base[1] + max_height*heightmap[x][y]
            z_coord = base[2] + step_y*y
            vertices.append((x_coord, y_coord, z_coord))
    return vertices