import vector
import math
import field
import display_helper
import matplotlib.pyplot as plt

cube_size=50

density=field.Density_field(cube_size,cube_size,cube_size,0.001)
density.generic_quad_cubes(101325*5,101325)
x_vals,y_vals,z_vals,vals=density.sparse_lattice(1,10)

fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

#ax.scatter(x_vals,y_vals,z_vals,marker='o')

for i in range(len(x_vals)):
    ax.plot(x_vals[i],y_vals[i],color=display_helper.get_rgb_density(vals[i]),marker="o")



ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

plt.show()
