# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class car:
    def __init__(self, name,model):
        self.name = name
        self.model = model
class ElectricCar(car):
    def __init__(self, name, model, battery_type):
        super().__init__(name, model)
        self.battery_type = battery_type

my_tesla = ElectricCar("Tesla","model S","85KWH")

print(isinstance(my_tesla, car)) # True
print(isinstance(my_tesla, ElectricCar)) # True
