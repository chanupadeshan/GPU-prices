import streamlit as st
import GPUprice as gpu
import re
# import os 

st.title('GPU price Scraper 📜')
st.write("This app scrapes the prices of the GPUs from Newegg.com. Enter the name of the GPU you are looking for and the app will scrape the prices of the GPUs from Newegg.com and save the results in an excel file.📊")
st.markdown("<hr>", unsafe_allow_html=True)

st.image("C:\projects\Web scraping\GPU-prices\gpu image.jpg")
user_input = st.text_input("What GPU are you Looking for?")
file_name = st.text_input("Enter the file name to save the results(only xlsx files are supported)")

pattern = f"\."
if re.search(pattern,file_name):
    split_name = file_name.split(".")[0]

else:
    split_name = file_name   

file_name = f"{split_name}.xlsx"

st.markdown("<hr>", unsafe_allow_html=True)

if st.button("Search"):
    st.write(f"Searching 🔎")
    gpu.scrap_gpu_price(user_input,file_name)
    st.write(f"Scraping Complete. Check the file {file_name} for the results.💯")

    with open(file_name, "rb") as file:
        button = st.download_button(label="Download",data=file,file_name=file_name,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    # file name is the name of the file to be downloaded
    # rb is read binary mode. this is very important to open the non-text files like spreadsheets, images etc.
    # data is the object to be downloaded. in this case it is the file object
    # file_name is the name of the file to be saved on the user's machine
    # mime is the type of file to be downloaded. In this case it is a spreadsheet file.