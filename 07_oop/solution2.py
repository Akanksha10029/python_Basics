# . Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class car:
    def __init__(self,start_name,end_name):
        self.start_name = start_name
        self.end_name = end_name

    def full_name(self):
        return f"{self.start_name} {self.end_name}"
my_car = car("Maruti","Suzuki")
print(my_car.full_name())