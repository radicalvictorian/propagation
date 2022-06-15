import vector
import vector.Vector as Vector

class Scalar_field:
    def __init__(self,x,y,z,grid_size):
        # NOTE grid size is in meters --- METRIC
        self.field=[[[0 for i in range(z)] for j in range(y)] for i in range(x)]
        self.grid_size=grid_size

    def sparse_lattice(self,spacing,z_slice):
        output_x=[]
        output_y=[]
        output_z=[]
        output_val=[]
        if z_slice == False:
            for x in range(0,len(self.field),spacing):
                for y in range(0,len(self.field[0]),spacing):
                    for z in range(0,len(self.field[0][0]),spacing):
                        output_x.append(x)
                        output_y.append(y)
                        output_z.append(z)
                        output_val.append(self.field[x][y][z])
        else:
            for x in range(0,len(self.field),spacing):
                for y in range(0,len(self.field[0]),spacing):
                    output_x.append(x)
                    output_y.append(y)
                    output_z.append(z_slice)
                    output_val.append(self.field[x][y][z_slice])
        return output_x,output_y,output_z,output_val


class Density_field(Scalar_field):
    def generic_quad_cubes(self,density,surrounding_density):
        output=self.field
        for x in range(len(self.field)):
            for y in range(len(self.field[0])):
                for z in range(len(self.field[0][0])):
                    if (len(self.field)/6 < x < len(self.field)/3 or 2*len(self.field)/3 < x < 5*len(self.field)/6) and (len(self.field)/6 < y < len(self.field)/3 or 2*len(self.field)/3 < y < 5*len(self.field)/6):
                        output[x][y][z]=density
                    else:
                        output[x][y][z]=surrounding_density
        self.field=output


# format is x_pos,x_neg,y_pos,y_neg,z_pos
# z_neg,x_pos/y_pos/z_pos,x_pos/y_pos/z_neg,x_pos/y_neg/z_pos,
# x_neg/y_pos/z_pos,x_pos/y_neg/z_neg,x_neg/y_pos/z_neg,x_neg/y_neg/z_pos,x_neg/y_neg/z_neg
class Vector_field_14:
    def __init__(self,x,y,z,grid_size):
        basis_temp=[Vector(0,0,0) for i in range(6)]
        lindependent_temp=[Vector(0,0,0) for i in range(8)]

        self.basis=[[[basis_temp for i in range(z)] for j in range(y)] for i in range(x)]
        self.lindependent=[[[lindependent_temp for i in range(z)] for j in range(y)] for i in range(x)]
        self.grid_size=grid_size
