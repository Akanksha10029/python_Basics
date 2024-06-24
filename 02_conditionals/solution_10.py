# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

animal = input("Enter animal (dog OR cat):")
age = int(input(f"Enter {animal}'s age:"))

if animal == "dog":
    if age <= 2:
        print("puppy food")
    else:
        print("Senior Dog food")
elif animal == "cat":
    if age >= 5:
        print("Senior cat food")
    else:
        print("kitten food")        
