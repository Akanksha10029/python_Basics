# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def fuel_type(self):
        return "petrol or diesel"
class ElectricCar(car):
    def fuel_type(self):
        return "electric Charge"
    
car1 = car("Toyota","Black")
# print("car1 fuel type:",car1.fuel_type())
print(f"{car1.name} fuel type: {car1.fuel_type()}")

car2 = ElectricCar("Tesla","White")
# print("car2 fuel type:",car2.fuel_type())
print(f"{car2.name} fuel type: {car2.fuel_type()}")