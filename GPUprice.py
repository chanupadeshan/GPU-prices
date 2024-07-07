from bs4 import BeautifulSoup
import requests
import re
import csv
from openpyxl import Workbook


def scrap_gpu_price(search,file_name):
            url = f"https://www.newegg.com/p/pl?d={search}"
            page = requests.get(url).text
            doc = BeautifulSoup(page, "html.parser")

            page_text = doc.find(class_="list-tool-pagination-text")
            final_page = str(page_text).split("/")[1].split(">")[1].split("<")[0]
            print(f"Total Number of pages:{final_page}")

            wb = Workbook()
            ws = wb.active
            ws.append([f"Number of pages: {final_page}"])
            ws.append(["Item", "Price", "Shipping"])

            for page_num in range(1, int(final_page) + 1):
                page_url = f"https://www.newegg.com/p/pl?d={search}&page={page_num}"
                page_content = requests.get(page_url).text
                page_doc = BeautifulSoup(page_content, "html.parser")

                # Correct class name for item listing
                div = page_doc.find(class_="item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell")
                if div:
                    items = div.find_all(text=re.compile(search, re.IGNORECASE))
                    pattern = r'Free\s+Shipping'

                    for item in items:
                        print(item)

                        parent_price = item.find_parent(class_="item-container") # parent of the item is the item-container
                        price = parent_price.find("li", class_="price-current")
                        price_split_sign = str(price).split("/")[1].split(">")[1].split("<")[0]
                        price_split_amount = str(price).split("/")[1].split(">")[2].split("<")[0]
                        Total_price = f"{price_split_sign} {price_split_amount}"
                        print(price_split_sign, price_split_amount)

                        shipping = ""
                        parent_shipping = item.find_parent(class_="item-container")
                        if re.search(pattern, str(parent_shipping.text)):
                            print("Free Shipping")
                            shipping = "Free Shipping"
                        else:
                             print("No shipping information available")
                             shipping = "No shipping information available"
                        print("\n")

                        ws.append([item, Total_price, shipping])

                else:
                    print(f"No items found on page {page_num}")

            wb.save(file_name)
