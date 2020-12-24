import random
import math
import matplotlib.pyplot as plt

class Starpolygon():
    def __init__(self, num_sides=3, radius=1.0):
        self.num_sides = num_sides
        self.radius = radius
        self.color = [random.random() for _ in range(3)]
        self.posx = random.random() * 10
        self.posy = random.random() * 10
    
    def get_area(self):
        a  = math.pi/self.num_sides
        hb = self.radius * math.cos(a)
        b  = self.radius * math.sin(a) * 2
        A  = (b*hb)/2
        return self.num_sides * A
    
    def display(self):
        xs = []
        ys = []
        a = math.pi*2/self.num_sides
        for i in range(self.num_sides+1):
            xs.append(self.posx + self.radius * math.cos(i*a))
            ys.append(self.posy + self.radius * math.sin(i*a))
        plt.plot(xs,ys,c=self.color)

mystars = []

for i in range(10):
    sp = Starpolygon(num_sides=random.randint(3,10), radius=1+random.random()*3)
    mystars.append(sp)

plt.figure(figsize=(12,12))
plt.axis('equal')
for sp in mystars:
    sp.display()

plt.show()