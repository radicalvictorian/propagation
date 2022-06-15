class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def dot(self,other):
        first=self.x*other.x
        second=self.y*other.y
        third=self.z*other.z
        return first+second+third
