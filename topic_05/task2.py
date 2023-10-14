import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]["rate"]
    else:
        raise Exception("Помилка при отриманні курсу валюти")

def convert_currency(amount, currency_code):
    try:
        rate = get_exchange_rate(currency_code)
        converted_amount = amount / rate
        return converted_amount
    except Exception as e:
        return f"Помилка: {e}"

while True:
    try:
        amount = float(input("Введіть суму в гривнях: "))
        
        if amount <= 0:
            raise ValueError("Помилка: Сума повинна бути більше нуля.")
        
        currency_code = input("Введіть валюту для конвертації (EUR, USD, AED): ").upper()

        if currency_code in ["EUR", "USD", "AED"]:
            result = convert_currency(amount, currency_code)
            print(f"{amount} UAH = {result:.2f} {currency_code}")
        else:
            print("Код валюти введений невірно або дана валюта не підтримується. Спробуйте ще раз.")
    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Помилка: {e}")
