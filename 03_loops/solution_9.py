# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]
items.append("apple")
for item in items:
    if items.count(item) > 1:
        print(f"Duplicate found: {item}")
        print("count of duplicacies:",items.count(item))
        break
    