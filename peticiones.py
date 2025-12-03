import requests

url = "https://jocarsa.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
    html = response.text  # or response.content for bytes
    print(html)
except requests.exceptions.RequestException as e:
    print("Error fetching the page:", e)
