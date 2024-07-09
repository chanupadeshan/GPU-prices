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
            ws.append(["Item", "Price", "Shipping","rated out of 5","Number of reviews","link"])

            for page_num in range(1, int(final_page) + 1):
                page_url = f"https://www.newegg.com/p/pl?d={search}&page={page_num}"
                page_content = requests.get(page_url).text
                page_doc = BeautifulSoup(page_content, "html.parser")

                # Correct class name for item listing
                div = page_doc.find(class_="item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell")
                if div:
                    items = div.find_all(text=re.compile(search, re.IGNORECASE))
                    

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

                        #number of views
                        reviews = parent.find("div",class_= "item-info").find("a", class_="item-rating")        
                        if reviews and reviews.find("span",class_="item-rating-num"):
                             Number_of_reviews = reviews.find("span",class_="item-rating-num").text
                             Number_of_reviews= Number_of_reviews.split("(")[1].split(")")[0]
                             print(Number_of_reviews)
                        else:
                            print("No reviews found")              
                        
                        #inside link
                        getURL = parent.find("a", class_="item-title")
                        url = getURL['href']
                        print(url)
                        print("\n")
                        ws.append([item, Total_price,split_shipping,aria_label,Number_of_reviews,url])

                else:
                    print(f"No items found on page {page_num}")

            wb.save(file_name)
