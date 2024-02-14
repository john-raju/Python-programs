# Python program to check if a year is a leap year or not
year = 2000  # You can change this value to test other years

# Divided by 100 means century year (ending with 00)
# Century year divided by 400 is a leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
# Not divided by 100 means not a century year
# Year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")
# If not divided by both 400 (century year) and 4 (not century year), year is not a leap year
else:
    print(f"{year} is not a leap year")
