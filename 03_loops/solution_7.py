# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while(True):

    num = int(input("Enter any number:"))
    if num < 1 or num > 10:
        print("Please enter a number between 1 and 10 to stop this loop.")
    else:
        print("You entered a valid number to stop this loop.")