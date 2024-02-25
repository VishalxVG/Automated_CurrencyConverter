import requests

API_KEY = 'fca_live_pJghz4NFDjreJVdrI2wOAZnz2KfkGzE4ORCXk7vv'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["EUR","CAD","USD","AUD","INR"]

def convert_currency(base):
    currnecies = ",".join(CURRENCIES)   # => USD,CAD,EUR...
    url = f"{BASE_URL}&base_currency={base}&currencies={currnecies}"

    try:
        response = requests.get(url)
        data = response.json()  
        return data["data"]
    except :    
        print("Invalid Currency")
        return None

while True:
    base = input("Enter the base currency (q to quit): ").upper() 
    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue 
    rate = int(input("Enter the how much u want to convert :")) 
    
    del data[base]
    for ticker, value in data.items():
        finalValue = round((value * rate),2)

        print(f"{ticker} : {finalValue}")