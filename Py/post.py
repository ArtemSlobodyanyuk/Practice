import requests

url = "https://api.monobank.ua/bank/currency"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Коди валют:
    # 980 - гривня (UAH)
    # 840 - долар США (USD)
    # 978 - євро (EUR)

    print("Курс валют:")
    for item in data:
        if item["currencyCodeA"] in [840, 978] and item["currencyCodeB"] == 980:
            currency = "USD" if item["currencyCodeA"] == 840 else "EUR"
            print(f"{currency} до UAH:")
            print(f"  Купівля: {item.get('rateBuy', 'N/A')}")
            print(f"  Продаж: {item.get('rateSell', 'N/A')}")
            print(f"  Міжбанк: {item.get('rateCross', 'N/A')}\n")

else:
    print(f"Помилка при запиті: {response.status_code}")
