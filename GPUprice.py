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
            ws.append(["Item", "Price", "Shipping","rated out of 5","Number of reviews"])

            for page_num in range(1, int(final_page) + 1):
                page_url = f"https://www.newegg.com/p/pl?d={search}&page={page_num}"
                page_content = requests.get(page_url).text
                page_doc = BeautifulSoup(page_content, "html.parser")

                # Correct class name for item listing
                div = page_doc.find(class_="item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell")
                if div:
                    items = div.find_all(text=re.compile(search, re.IGNORECASE))
                    pattern = r'rating\s+rating-4-5'

                    for item in items:
                        print(item)

                        parent = item.find_parent(class_="item-container") # parent of the item is the item-container

                        #get price
                        price = parent.find("li", class_="price-current")
                        price_split_sign = str(price).split("/")[1].split(">")[1].split("<")[0]
                        price_split_amount = str(price).split("/")[1].split(">")[2].split("<")[0]
                        Total_price = f"{price_split_sign} {price_split_amount}"
                        print(price_split_sign, price_split_amount)

                         #get shipping
                        shipping = parent.find("li",class_="price-ship")
                        split_shipping = str(shipping).split(">")[1].split("<")[0]
                        print(split_shipping)
               
                        #get rated out of 5
                        itemrating = parent.find("div", class_="item-info").find("a", class_="item-rating")
                        if itemrating and itemrating.find("i", class_="rating"):
                            aria_label = itemrating.find("i", class_="rating")['aria-label']
                            print(aria_label)
                        else:
                            print("No rating found")
                        # if str(itemrating.has_attr("aria-label")):s
                        #     print(itemrating["aria-label"])
                        # else:
                        #      print("No rating found")
                        
                        print("\n")
                        ws.append([item, Total_price,split_shipping,aria_label])

                else:
                    print(f"No items found on page {page_num}")

            wb.save(file_name)
