class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return vec3(self.x+v.x, self.y+v.y, self.z+v.z)
    
    def __sub__(self, v):
        return vec3(self.x-v.x, self.y-v.y, self.z-v.z)
    
    def __mul__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x*v.x, self.y*v.y, self.z*v.z)
        else:
            return vec3(self.x*v, self.y*v, self.z*v)
    
    def __truediv__(self, s):
        return self * (1/s)
    
    def __str__(self):
        return f"vec3({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z
    
    def dot(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z
    
    def cross(self, v):
        return vec3(self.y*v.z - self.z*v.y, self.z*v.x - self.x*v.z, self.x*v.y - self.y*v.x)
    
    def length_squared(self):
        return self.dot(self)
    
    def length(self):
        return self.length_squared() ** 0.5
    
    def unit_vector(self):
        return self / self.length()