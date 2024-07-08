# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

class Battery:
    def battery_info(self):
        return ("Battery Battery!!")
        
class Engine:
    def engine_info(self):
        return ("Engine Engine!!")

class ElectricCar(car, Battery, Engine):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color
    
    def car_info(self):
        return f"{self.name} {self.model} in {self.color} color"
    
    def full_info(self):
        return f"{self.car_info()}\n{self.engine_info()}\n{self.battery_info()}"

# Create an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "Red")

# Print the car's information
print(my_tesla.car_info())

# Print the car's engine and battery information
print(my_tesla.engine_info())
print(my_tesla.battery_info())

# # Print the full information
print(my_tesla.full_info())