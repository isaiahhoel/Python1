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
# Assignment: Chapter # 2 Project # 10
# Date: 08/27/2021
# ---------------------------------------------------
hourlyWage = float(input("Enter hourly wage:"))
hoursWorked = int(input("Enter regular hours Worked:"))
overtimeHours = int(input("Enter amount of overtime hours:"))
regularPay = float(hourlyWage * hoursWorked)
overtimePay = float(overtimeHours * (hourlyWage * 1.5))
weeklyPay = round((overtimePay + regularPay), 2)
print("Your total pay this week is ", "$", weeklyPay)