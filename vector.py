import math

def init_vector_field(x,y,z):
    x_vectors=[[[0 for i in range(z)] for j in range(y)] for i in range(x)]
    y_vectors=[[[0 for i in range(z)] for j in range(y)] for i in range(x)]
    z_vectors=[[[0 for i in range(z)] for j in range(y)] for i in range(x)]
    return x_vectors,y_vectors,z_vectors

def init_generic_field(x,y,z):
    output=[[[0 for i in range(z)] for j in range(y)] for i in range(x)]
    return output


# takes in a generic field and outputs x and y coordinates for plotting of a sparse lattice
def sparse_lattice(field,spacing,z_slice):
    output_x=[]
    output_y=[]
    output_z=[]
    output_val=[]
    if z_slice == False:
        for x in range(0,len(field),spacing):
            for y in range(0,len(field[0]),spacing):
                for z in range(0,len(field[0][0]),spacing):
                    output_x.append(x)
                    output_y.append(y)
                    output_z.append(z)
                    output_val.append(field[x][y][z])
    else:
        for x in range(0,len(field),spacing):
            for y in range(0,len(field[0]),spacing):
                output_x.append(x)
                output_y.append(y)
                output_z.append(z_slice)
                output_val.append(field[x][y][z_slice])
    return output_x,output_y,output_z,output_val


# density setter functions for initial conditions
def generic_spherical_density(field):
    output=field
    for x in range(len(field)):
        for y in range(len(field[0])):
            for z in range(len(field[0][0])):
                precursor_1=(len(field)**2+len(field)**2+len(field)**2)**(1./2.)
                precursor_2=((x-len(field)/2)**2+(y-len(field[0])/2)**2+(z-len(field[0])/2)**2)**(1./2.)
                output[x][y][z]=round(precursor_1-precursor_2,2)
    return field

def generic_twin_cubes(field):
    output=field
    for x in range(len(field)):
        for y in range(len(field[0])):
            for z in range(len(field[0][0])):
                if (len(field)/6 < x < len(field)/3 or 2*len(field)/3 < x < 5*len(field)/6) and (len(field)/6 < y < len(field)/3 or 2*len(field)/3 < y < 5*len(field)/6):
                    output[x][y][z]=101325*5
                else:
                    output[x][y][z]=101325
    return output


def get_rgb_density(density):
    if density > 101325*4.5:
        output=(1,0,0)
    elif density > 101325*3.5:
        output=(0.5,0.5,0)
    elif density > 101325*2.5:
        output=(0,1,0)
    elif density > 101325*1.25:
        output=(0,0.5,0.5)
    else:
        output=(0,0,1)
    return output
