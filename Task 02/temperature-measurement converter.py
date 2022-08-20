# Make a temperature/measurement converter.
# Write a script that can convert Fahrenheit to Celcius and back,
# or inches to centimeters and back, etc


def temperature(temp):
    temp = temp.split(" ")
    #print(temp)
    unit = temp[-1].lower()
    #print(unit)
    value = int(temp[0])
    #print(value)
    if unit[0] == "c":
        new_value = (value *1.8) + 32
        print(f"the result = {new_value} F ")
    elif unit[0] == "f":
        new_value = round((value - 32)*0.5556)
        print(f"the result = {new_value} C ")
    else:
        print("please enter correct temperature unit (C ,F)")


def measurement(measure):
    measure = measure.split(" ")
    unit = measure[-1].lower()
    value = int( measure[0])
    if unit[0] == "c":
        new_value = round(value / 2.54, 1)
        print(f"the result = {new_value} inch ")
    elif unit[0] == "i":
        new_value = round(value * 2.54, 1)
        print(f"the result = {new_value} cm ")
    else:
        print("please enter correct measurement unit (cm ,inch)")


print("Welcome to temperature/measurement converter game ")
type_used = int(input("what you want to convert \n\t1- Temperature\n\t2- Measurement \n>> "))

if type_used == 1 :
    temp = input("Enter the tempetrature you want to convert ,( Ex 210 C or 50 F )\n>> ")
    temperature(temp)
elif type_used == 2:
    measure = input("Entre the measurement you want to convert ,( Ex 15 inch or 20 cm ) \n>> ")
    measurement(measure)
else :
    print("Please Enter 1 or 2 only ")


