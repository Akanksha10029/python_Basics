# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

string = input("Enter any string:")
for str in string:
    print(str)
    if string.count(str) == 1:
        print("First non-repeated character is: ", str)
        break