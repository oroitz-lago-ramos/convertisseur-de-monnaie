from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes


def get_money_symbol(code):
    c = CurrencyCodes()
    return c.get_symbol(code)

def convert(current,wished,amount):
    c = CurrencyRates()
    return c.convert(current, wished, amount)

def save_conversion_history(actual_currency, wished_currency, amount, final_amount):
    with open('conversion_history.txt', 'a') as file:
        file.write(f"{amount} {actual_currency} ----> {final_amount:.2f} {wished_currency}\n")

