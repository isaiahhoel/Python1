# ---------------------------------------------------
# Hannibal-LaGrange University
# CSC 303 - Program Design
# Fall 2021
# Instructor: Mr. Hammontree 
#
# Student: Hoelscher, Isaiah
# Student ID: A0000033934
# Student Email: isaiah.hoelscher.18@student.hlg.edu
#
# Assignment: Chapter 3 project 7
# Date: 09/03/2021
# ---------------------------------------------------


startSalary = int(float(input("Enter Starting Salary: ")))
percentIncrease = int(input("Enter percent increase:"))
yearsWorked = int(input("Enter years worked:"))


percentIncrease = percentIncrease / 100

totalPercent = 0.0

print("%4s%10s" % \
("Years Worked", "Salary"))
print("-" * 25)

for year in range(1, 10):
    salaryIncrease = startSalary * percentIncrease
    newSalary = startSalary + salaryIncrease
    print("%3d%21.2f" % \
    (year, startSalary))
    startSalary = newSalary
    totalPercent += percentIncrease

for year in range(10, yearsWorked + 1):
    print("%3d%21.2f" % \
    (year, startSalary))