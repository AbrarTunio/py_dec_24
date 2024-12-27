age = input("Enter your age: ")

try:
    int_age = int(age)
except:
    int_age = -1

fage = int_age + 20

print("Your father's age is: " , fage)