from inputs import *
from conversion import *

def main():
    actual_currency = input_country()
    wished_currency = input_country()
    amount = input_amount()
    
    actual_symbol = get_money_symbol(actual_currency)
    wished_symbol = get_money_symbol(wished_currency)
    
    final_amount = convert(actual_currency, wished_currency, amount)
    
    print(f"{amount} {actual_symbol} ----> {final_amount:.2f} {wished_symbol}")
    save_conversion_history(actual_currency, wished_currency, amount, final_amount)

if __name__ == '__main__':
    main()
