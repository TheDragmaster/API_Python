import requests 

user_input = str(input("What cryptocurrency would you like information for ? "))

response = requests.get("https://api.coincap.io/v2/assets/"+user_input.lower())

if response.status_code != 200:
    print("Error trying to retrieve data.")
else:
    print("Cryptocurrency: ", response.json()['data']['name'])
    print("Symbol: ", response.json()['data']['symbol'])
    print("Rank: ",response.json()['data']['rank'])
    print("Circulating Supply: ", response.json()['data']['supply'])
    print("Market cap (USD):", response.json()['data']['marketCapUsd'])
    print("Price (USD): ", response.json()['data']['priceUsd'])