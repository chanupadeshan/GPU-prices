from bs4 import BeautifulSoup
import requests
import re

input("What GPU are you looking for? ")

url = f"https://www.newegg.com/p/pl?d={input}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text")
final_page = str(page_text).split("/")[1].split(">")[1].split("<")[0]


for page in range(1,final_page+1):
    url = f"https://www.newegg.com/p/pl?d={input}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")