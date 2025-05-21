import streamlit as st
import base64
import requests

st.title("My Resume")

# Use the raw GitHub URL for the PDF
pdf_url = "https://raw.githubusercontent.com/NickJordan-BE/PortfolioWebsite/main/client/static/NickJordanResumeML.pdf"
response = requests.get(pdf_url)

if response.status_code == 200:
    base64_pdf = base64.b64encode(response.content).decode('utf-8')

    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.error("Failed to load PDF.")
