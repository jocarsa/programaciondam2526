import requests
from lxml import html

url = "https://elpais.com"

response = requests.get(url, timeout=10)
response.raise_for_status()

tree = html.fromstring(response.content)

# 1. Web title
title = tree.xpath("//title/text()")
print("WEB TITLE:")
print(title[0] if title else "No title found")

# 2. Links href
print("\nLINKS:")
links = tree.xpath("//a/@href")

for i, href in enumerate(links, start=1):
    print(f"{i}: {href}")
