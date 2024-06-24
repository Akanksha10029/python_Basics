# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score:"))
if 90 <= score <=100 :
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 60 <= score <= 69:
    print("Your grade is D")
else:
    print("Your grade is F")