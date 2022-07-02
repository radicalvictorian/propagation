import random
import vector





class Ideal_Gas:
    def __init__(self,number,max_velocity,bound,timestep,interaction_radius):
        self.velocity_vectors=[]
        self.position_vectors=[]
        for i in range(number):
            x_vel=random.randint(0,max_velocity)
            y_vel=random.randint(0,max_velocity)
            z_vel=random.randint(0,max_velocity)

            x_0=random.randint(0,bound)
            y_0=random.randint(0,bound)
            z_0=random.randint(0,bound)

            vel_vectors=vector.Vector(x_vel,y_vel,z_vel)
            pos_vectors=vector.Vector(x_0,y_0,z_0)
            self.velocity_vectors.append(vel_vectors)
            self.position_vectors.append(pos_vectors)

        self.number=number
        self.max_velocity=max_velocity
        self.bound=bound
        self.timestep=timestep
        self.interaction_radius=interaction_radius

    def get_coords(self):
        x_coords=[]
        y_coords=[]
        z_coords=[]

        for i in self.position_vectors:
            x_coords.append(i.x)
            y_coords.append(i.y)
            z_coords.append(i.z)

        return x_coords,y_coords,z_coords


    def get_velocities(self):
        x_vect=[]
        y_vect=[]
        z_vect=[]

        for i in self.velocity_vectors:
            x_vect.append(i.x)
            y_vect.append(i.y)
            z_vect.append(i.z)

        return x_vect,y_vect,z_vect




    def update_positions(self):
        x_pos=[]
        y_pos=[]
        z_pos=[]

        x_vel=[]
        y_vel=[]
        z_vel=[]

        for i in range(len(self.velocity_vectors)):
            x_pos.append(self.velocity_vectors[i].x*self.timestep+self.position_vectors[i].x)
            y_pos.append(self.velocity_vectors[i].y*self.timestep+self.position_vectors[i].y)
            z_pos.append(self.velocity_vectors[i].z*self.timestep+self.position_vectors[i].z)

            x_vel.append(self.velocity_vectors[i].x)
            y_vel.append(self.velocity_vectors[i].y)
            z_vel.append(self.velocity_vectors[i].z)


        for i in range(len(x_pos)):
            if x_pos[i] < 0:
                x_pos[i] = abs(x_pos[i])
                x_vel[i] = -1*x_vel[i]
            elif x_pos[i] > self.bound:
                x_pos[i] = self.bound - self.timestep*x_vel[i]
                x_vel[i] = -1*x_vel[i]
            
            if y_pos[i] < 0:
                y_pos[i] = abs(y_pos[i])
                y_vel[i] = -1*y_vel[i]
            elif y_pos[i] > self.bound:
                y_pos[i] = self.bound - self.timestep*y_vel[i]
                y_vel[i] = -1*y_vel[i]
            
            if z_pos[i] < 0:
                z_pos[i] = abs(z_pos[i])
                z_vel[i] = -1*z_vel[i]
            elif z_pos[i] > self.bound:
                z_pos[i] = self.bound - self.timestep*z_vel[i]
                z_vel[i] = -1*z_vel[i]

        for i in range(len(self.velocity_vectors)):
            self.velocity_vectors[i].x=x_vel[i]
            self.velocity_vectors[i].y=y_vel[i]
            self.velocity_vectors[i].z=z_vel[i]

            self.position_vectors[i].x=x_pos[i]
            self.position_vectors[i].y=y_pos[i]
            self.position_vectors[i].z=z_pos[i]