from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes


def get_money_symbol(code):
    c = CurrencyCodes()
    return c.get_symbol(code)

def convert(current,wished,amount):
    c = CurrencyRates()
    return c.convert(current, wished, amount)
