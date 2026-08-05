import requests

url = "https://api.adviceslip.com/advicea"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    
    print(response.status_code)

    print(response.text)

    data = response.json()
    print(data["slip"]["advice"])

except requests.exceptions.RequestException as err:
    print(f"An error occured: {err}")