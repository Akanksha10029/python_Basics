# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

Age = int(input("Enter your age:"))

if Age < 13:
    print("Child")
elif   13 <= Age <=19:
    print("Teenager")
elif   20 <= Age <=59:
    print("Adult")
else:
    print("Senior")    