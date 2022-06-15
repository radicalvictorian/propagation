
# Import a library of functions called 'pygame'
import pygame
import vector
import math
import matplotlib.pyplot as plt
import iterate

cube_size=100

vector_field=vector.init_vector_field(cube_size,cube_size,cube_size)
print('vector field set up')
density_field=vector.init_generic_field(cube_size,cube_size,cube_size)
print('density field set up')
#density_field=vector.generic_spherical_density(density_field)
density_field=vector.generic_twin_cubes(density_field)
print('density field filled')
x_vals,y_vals,z_vals,vals=vector.sparse_lattice(density_field,1,50)
print('sparse lattice created')


fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

#ax.scatter(x_vals,y_vals,z_vals,marker='o')

for i in range(len(x_vals)):
    ax.plot(x_vals[i],y_vals[i],color=vector.get_rgb_density(vals[i]),marker="o")



ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

plt.show()













"""
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653


# Set the height and width of the screen
size = (200,200)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    for i in range(0,50):
        pygame.draw.line(screen, BLACK, (i,50), (i,50))


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.

    clock.tick(60)

# Be IDLE friendly
pygame.quit()
"""
