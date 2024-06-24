# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

psd = input("Enter your password:")
if len(psd) < 6:
    print("Weak password")
elif 6 <= len(psd) <= 10:
    print("Medium password")
else:
    print("Strong password")