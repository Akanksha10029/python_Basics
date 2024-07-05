# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(car):
    def __init__(self,brand,model,battery_size):
        self.batter_size = battery_size
        super().__init__(brand,model)
        
my_tesla = ElectricCar("Tesla","Model S","85KWH")

print(my_tesla.model)
print(my_tesla.full_name())