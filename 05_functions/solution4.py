# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def arcircum(radius):
    area = math.pi * radius ** 2
    circumferance = 2 * math.pi * radius
    return area,circumferance

radius  = float(input("Enter radius:"))
area, circumference = arcircum(radius)

print(f"Area: {area:.2f} and Circumference: {circumference:.2f}")
