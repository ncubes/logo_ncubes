import numpy as np
from stl import mesh

# Define the 8 vertices of the cube
# In total, 8 cubes must be defined, so this list will be expanded
# Symbols will subsitute for the numbers here. The symbols will pick
# numbers from the 4 dimensional points in the input cube.
# the input file to the program merely consists of the coordinates
# of each of the vertices in order [0,0,0,1], .. [1,1,1,1].
# to start with the 3d case will be symbolized.
vertices = np.array([\
    [0, 0, 0], #0
    [+1, 0, 0],#1
    [+1, +1, 0], #2
    [0, +1, 0], #3
    [0, 0, +1],
    [+1, 0, +1],
    [+1, +1, +1],
    [0, +1, +1]])


# Define the 12 triangles composing the cube
# This list can be made longer, so total size for 4-cube would be
# in lines of code, 12 * 8 since there are eight faces on a 4-cube.
faces = np.array([\
    [0,3,1],
    [1,3,2],
    [0,4,7],
    [0,7,3],
    [4,5,6],
    [4,6,7],
    [5,1,2],
    [5,2,6],
    [2,3,6],
    [3,7,6],
    [0,1,5],
    [0,5,4],])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    print ("i = ", i)
    for j in range(3):
        print ("j =",j)
        cube.vectors[i][j] = vertices[face[j],:]
        print ("verices[face[j],:]",vertices[face[j],:2])
print ("cube.vectors",cube.vectors)
# Write the mesh to file "cube.stl"
print (cube)
cube.save('cube.stl')
