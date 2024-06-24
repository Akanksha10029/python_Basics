# 2. Movie Ticket Pricing

# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

Age = int(input("Enter your Age:"))
Day = input("Enter day:")

price = 12 if Age >= 18 else 8
if Day == "wednesday" :
        price = price -2
print("Your ticket price is $",price)
       