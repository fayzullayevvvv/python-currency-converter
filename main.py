import json
import requests


def converter(amount: float, currency: str) -> float:
    response = requests.get(f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/{currency.upper()}/')

    rate = float(json.loads(response.text)[0]['Rate'])

    result = amount * rate
    return result


def main() -> None:
    amount = float(input("Amount: "))
    currency = input("Currency: ")

    result = converter(amount, currency)

    print(f"{result:,.2f}")

main()
