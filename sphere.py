import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

sphere = Sphere(5)

volume = sphere.volume()
print(f"The volume of the sphere with radius {sphere.radius} is {volume:.2f}")