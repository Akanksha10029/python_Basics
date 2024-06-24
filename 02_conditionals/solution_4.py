# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = input(f"Enter color of {fruit}:")
if color == "Green" or color == "green":
    print("Unripe")
elif color == "Yellow" or color == "yellow":
    print("Ripe")
elif color == "Brown" or color == "brown":
    print("Overripe")