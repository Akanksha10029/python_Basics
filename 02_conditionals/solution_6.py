# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

dist = int(input("Enter distance to travel in km:"))
if dist <3 :
    print("Walk")
elif 3 <= dist <= 15 :
    print("Bike")
else:
    print("Car")