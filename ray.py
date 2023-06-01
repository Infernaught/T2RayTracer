from vec3 import vec3

class ray:
    def __init__(self, origin=vec3(), direction=vec3()):
        self.origin = origin
        self.direction = direction
    
    def at(self, t):
        return self.origin + self.direction * t