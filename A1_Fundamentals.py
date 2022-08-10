# TODO : take data from the user
# height = int(input("Enter Your Height : "))
# color = input("Enter Your Fav Color")

# Arithmetic operation 
# TODO : Adds 2 to a and assigns the result to b
# a = 12
# a += 2
# b = a

# TODO Multiplies b times 4 and assigns the result to a
# a = b * 4

# TODO Divides a by 3.14 and assigns the result to b
# b = a / 3.14
# b = a / 3.14

# TODO Subtracts 8 from b and assigns the result to a
# a = b - 8

# TODO : change number format
# number = 1234567.456
# print(format(number, ',.1f'))

# George@John@Paul@Ringo

# ----------------------------------------------------------------------------------
# todo Ex.1 Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the
# price of each item, and then displays the subtotal of the sale, the amount of sales
# tax, and the total. Assume the sales tax is 6 percent.

total = 0
for i in range(5):
    price = int(input(f"Enter the price of product num {i+1} :$"))
    total += price
tax = total * 6 / 100
print(f"Tax = {tax}")
print(f"Total Purchase = {total + tax}")

# -----------------------------------------------------------------------------
# todo Ex.2 Miles-per-Gallon
# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# Write a program that asks the user for the number of miles driven and the gallons
# of gas used. It should calculate the car’s MPG and display the result.

miles_driven = int(input("Enter the number of miles driven :  "))
gallons_of_gas = int(input("Enter the number of Gallon of Gas used"))
MPG = miles_driven / gallons_of_gas
print(f"Miles-per-Gallon = {format(MPG, '.2f')}")
