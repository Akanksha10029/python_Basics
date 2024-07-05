# . Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class car:
    def __init__(self,startName,endName):
        self.startName = startName
        self.endName = endName

    def fullName(self):
        return f"{self.startName} {self.endName}"
my_car = car("Maruti","Suzuki")
print(my_car.fullName())