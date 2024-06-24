# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter coffee size:")
order_shot = input("Would you like an extra shot of espresso? (yes/no):")
if order_shot == "yes":
    shot = "with an extra shot of espresso"
elif order_shot == "no":
    shot = ""

print(f"{order_size} coffee",shot)    