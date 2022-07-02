import vector
import surface
import gas

import math
import pygame
import time




#number,max_velocity,bound,timestep,interaction_radius
gas = gas.Ideal_Gas(7,8,900,0.02,0.5)

x,y,z=gas.get_coords()

pygame.init()
screen = pygame.display.set_mode((900,900))
screen.fill((255,255,255))

while True:
    gas.update_positions()
    x,y,z=gas.get_coords()

    screen.fill((255,255,255))

    for i in range(len(x)):
        pygame.draw.circle(screen,(0,0,0),(x[i],y[i]),5)
    
    pygame.display.update()
