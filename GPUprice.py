from bs4 import BeautifulSoup
import requests
import re
# from bs4 import BeautifulSoup
# import requests

# search = input("What GPU are you looking for? ")

# url = f"https://www.newegg.com/p/pl?d={search}"
# page = requests.get(url).text
# doc = BeautifulSoup(page, "html.parser")

# page_text = doc.find(class_="list-tool-pagination-text")
# final_page = str(page_text).split("/")[1].split(">")[1].split("<")[0]
# print(final_page)

# for page_num in range(1, int(final_page) + 1):
#     page_url = f"https://www.newegg.com/p/pl?d={search}&page={page_num}"
#     page_content = requests.get(page_url).text
#     page_doc = BeautifulSoup(page_content, "html.parser")

#     # Correct class name for item listing
#     div = page_doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
#     if div:
#         items = div.find_all("a", class_="item-title")
#         for item in items:
#             print(item)
#     else:
#         print(f"No items found on page {page_num}")

search = input("What GPU are you looking for? ")

url = f"https://www.newegg.com/p/pl?d={search}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text")
final_page = str(page_text).split("/")[1].split(">")[1].split("<")[0]
print(final_page)

for page_num in range(1, int(final_page) + 1):
    page_url = f"https://www.newegg.com/p/pl?d={search}&page={page_num}"
    page_content = requests.get(page_url).text
    page_doc = BeautifulSoup(page_content, "html.parser")

    # Correct class name for item listing
    div = page_doc.find(class_="item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell")
    if div:
        # items = div.find_all(text=re.compile(search, re.IGNORECASE))
        items = div.find_all(text=re.compile(search, re.IGNORECASE))
        for item in items:
            print(item)

            parent_price = item.find_parent(class_="item-container")
            price  = parent_price.find("li", class_="price-current")
            price_split_sign = str(price).split("/")[1].split(">")[1].split("<")[0]
            price_split_amount = str(price).split("/")[1].split(">")[2].split("<")[0]
            # print(price_split_sign)
            print(price_split_sign,price_split_amount)
            print("\n")


    else:
        print(f"No items found on page {page_num}")
