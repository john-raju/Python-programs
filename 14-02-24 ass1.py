# Input employee details
emno = 101
empname = "John Doe"
designation = "Software Engineer"
basic = 50000
hra = 10000
da = 8000
ta = 3000

# Calculate net salary
netsalary = basic + da + ta + hra

# Determine tax based on net salary
if netsalary > 50000:
    tax = 0.05 * netsalary
elif netsalary > 35000:
    tax = 0.03 * netsalary
elif netsalary > 20000:
    tax = 0.01 * netsalary
else:
    tax = 0

# Print employee details and salary bill
print(f"Employee Number: {emno}")
print(f"Employee Name: {empname}")
print(f"Designation: {designation}")
print(f"Basic Salary: {basic}")
print(f"HRA: {hra}")
print(f"DA: {da}")
print(f"TA: {ta}")
print(f"Net Salary: {netsalary}")
print(f"Tax: {tax}")
