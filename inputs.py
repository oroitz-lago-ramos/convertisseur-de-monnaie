countries_list = ['EUR','IDR','BGN', 'ILS', 'GBP', 'DKK','CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL','PLN', 'PHP', 'ZAR']

def print_list():
    print(" |EUR - Euro Member Countries\n |IDR - Indonesia Rupiah\n |BGN - Bulgaria Lev\n |ILS - Israel Shekel\n |GBP - United Kingdom Pound\n |DKK - Denmark Krone\n |CAD - Canada Dollar\n |JPY - Japan Yen\n |HUF - Hungary Forint\n |RON - Romania New Leu\n |MYR - Malaysia Ringgit\n |SEK - Sweden Krona\n |SGD - Singapore Dollar\n |HKD - Hong Kong Dollar\n |AUD - Australia Dollar\n |CHF - Switzerland Franc\n |KRW - Korea (South) Won\n |CNY - China Yuan Renminbi\n |TRY - Turkey Lira\n |HRK - Croatia Kuna\n |NZD - New Zealand Dollar\n |THB - Thailand Baht\n |USD - United States Dollar\n |NOK - Norway Krone\n |RUB - Russia Ruble\n |INR - India Rupee\n |MXN - Mexico Peso\n |CZK - Czech Republic Koruna\n |BRL - Brazil Real\n |PLN - Poland Zloty\n |PHP - Philippines Peso\n |ZAR - South Africa Rand\n")

def input_country():
    while True:
        money_code = input("Rentrez le code pays de votre choix, entrez liste pour afficher la liste: ")
        if money_code == 'liste':
            print_list()
        elif money_code in countries_list:
            return money_code
        else:
            print("Code pays invalide. Veuillez vérifier la liste")

def input_amount():
    while True:
        try: 
            return int(input("Combien voulez vous échanger: "))
        except:
            print("Veuillez rentrer un quantité valide")