# 0.1 Decision Statements

from math import pi
radius = eval(input("Enter radius of a circle: "))

if radius > 0:
    area = pi * radius * radius
    print("Area of the circule is = ", format(area,".2f"))
    circumference = 2*pi*radius
    print("Circumference of the circule is = ", format(circumference,".2f"))
else:
    print("Please give right input")

# 1 Check if a variable is a string using isinstance()

# x = 10
# tst = isinstance(x, int)
# print(tst)

# x = "string"
# tst = isinstance(x, str)
# print(tst)


# sales = float(input("Enter total sales of the month"))
# basic = 4000



# sales = float(input("Enter total sales of the month"))
# basic = 4000

# 1

# conveyance = 500
# da = 110 * basic/100
# if sales >= 100000:
#     hra = 20 * basic/100
#     incentive = sales * 10/100
#     bonus = 1000
# else:
#     hra = 10 * basic/100
#     incentive = sales * 4/100
#     bonus = 500

# salary = basic+hra+incentive+bonus+conveyance+da
# print("Salary Receipt of Employee")
# print(" Total Sales", sales)
# print(" Basic = ", basic)
# print(" HRA = ", hra)
# print(" Da = ", da)
# print(" Incentive = ", incentive)
# print(" Bonus = ", bonus)
# print(" Conveyance = ", conveyance)


# PROGRAM 3: Write a program that prompts a user to enter two different numbers. Perform basic
# arithmetic operations based on the choices.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
print("Which operation you want to: ")
print("1) Addition")
print("2) Substraction")
print("3) Multiplication")
print("4) Division")

2

choice = int(input("Enter your choice: "))
if choice == 1:
    text = f"Addition of {first_number} and {second_number} is: {first_number + second_number}"
    print(text)
elif choice == 2:
    text = f"Substraction between {first_number} and {second_number} is:{first_number - second_number}"
    print(text)
elif choice == 3:
    text = f"Multiplication of {first_number} and {second_number} is:{first_number * second_number}"
    print(text)
elif choice == 4:
    text = f"Division of {first_number} and {second_number} is: {first_number / second_number}"
    print(text)