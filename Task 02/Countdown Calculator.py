# Build a countdown calculator.
# Write some code that can take two dates as input,
# and then calculate the amount of time between them

from datetime import date
today = date.today()
print("Welcome to my countdown calculator")
print(f"We recognize only this formate of time {today}")

f_date =list(map(lambda a : int(a),input("Enter The First date ....\n>>").split("-")))
s_date =list(map(lambda a : int(a),input("Enter The Second date ....\n>>").split("-")))


f_ = date(f_date[0],f_date[1],f_date[2])
s_ = date(s_date[0],s_date[1],s_date[2])

amount = s_ - f_
print(f" the amount between two dates = {amount}")












