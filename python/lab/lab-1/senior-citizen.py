import datetime as dt

name = input("Enter your name: ")
yob = int(input("Enter your Year of Birth: "))

age = dt.datetime.now().year - yob

if age >= 60:
    print(f"{name} is a senior citizen.")
else:
    print(f"{name} is not a senior citizen.")

# The code takes a name and year of birth as input, calculates the age, and checks if the person is a senior citizen (60 years or older).
# The code uses the datetime module to get the current year and perform the calculation.

