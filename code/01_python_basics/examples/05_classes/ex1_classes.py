class Vehicle():
    def __init__(self, colour, nb_wheels, name):
        self.colour = colour
        self.nb_wheels = nb_wheels
        self.name = name

vehicle_1 = Vehicle("blue", 2, "bike")
vehicle_2 = Vehicle("red", 4, "car")

print("This is a " + vehicle_1.colour + " " + vehicle_1.name + " with ", vehicle_1.nb_wheels, " " + "wheels")
print("This is a " + vehicle_2.colour + " " + vehicle_2.name + " with " + str(vehicle_2.nb_wheels) + " " + "wheels")