# Currency converter :
# create a python script that takes a money with currency
# and convert it to some other currencies ,
# the code should be like the game we did before
from forex_python.converter import CurrencyRates

def currency_converter(money_amount, from_currency ,to_currency):
    currency_rate = CurrencyRates()
   
    new_amount = currency_rate.convert(from_currency, to_currency, money_amount)
    return new_amount

amount = float(input("Enter the money amount you want to convert :\n>>"))
from_currency = input("Enter the currency from which you will convert :\n>>").upper()
to_currency = input("Enter the currency to which you will convert :\n>>").upper()
print(f"The converted rate is:{currency_converter(amount, from_currency, to_currency )}" )
