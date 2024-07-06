# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class car:
    num_of_cars = 0
    def __init__(self, name, color):
        self.model = name
        self.color = color
        car.num_of_cars += 1
car1 = car("Toyota","Black")
car2 = car("Tata","silver")
car3 = car("Safari","Red")
print(f"Total cars created: {car.num_of_cars}")