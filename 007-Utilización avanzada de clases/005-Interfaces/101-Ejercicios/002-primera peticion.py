# pip3 install requests --break-system-packages
import requests

url = "https://jocarsa.com"

try:
    response = requests.get(url, timeout=10)

    print("Status code:", response.status_code)
    print("Final URL:", response.url)
    print("Headers:", response.headers)
    print("First 500 characters of body:\n")
    print(response.text[:500])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)