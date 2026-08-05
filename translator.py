import requests

url = "https://api.mymemory.translated.net/get"

payload = {
    "q": "Excuse me, I'm out of rhythm",
    "langpair": "en|es",
}

try:
    response = requests.get(url, params=payload, timeout=5)
    print(response.status_code)
    print(response.text)
    response.raise_for_status()
    
    result = response.json()
    translated_text = result["responseData"]["translatedText"]
    print(f"Original: {payload['q']}")
    print(f"Result: {translated_text}")

except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")