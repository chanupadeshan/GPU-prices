from bs4 import BeautifulSoup
import requests
import re

input("What GPU are you looking for? ")

url = f"https://www.newegg.com/p/pl?d={input}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text")
print(page_text)