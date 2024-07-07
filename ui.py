import streamlit as st
import GPUprice as gpu
import re

st.title('GPU price Scraper 📜')
st.image("C:\projects\Web scraping\GPU-prices\gpu image.jpg")
user_input = st.text_input("What GPU are you Looking for?")
file_name = st.text_input("Enter the file name to save the results(only xlsx files are supported)")

pattern = f"\."
if re.search(pattern,file_name):
    split_name = file_name.split(".")[0]

else:
    split_name = file_name   

file_name = f"{split_name}.xlsx"

if st.button("Search"):
    st.write(f"Searching 🔎")
    gpu.scrap_gpu_price(user_input,file_name)
    st.write(f"Scraping Complete. Check the file {file_name} for the results.💯")

