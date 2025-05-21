import streamlit as st
import base64
import requests

st.title("My Resume")

pdf_url = "https://raw.githubusercontent.com/NickJordan-BE/PortfolioWebsite/main/client/static/NickJordanResumeML.pdf"
response = requests.get(pdf_url)

if response.status_code == 200:
    base64_pdf = base64.b64encode(response.content).decode('utf-8')
    
    # Use iframe instead of embed
    pdf_display = f"""
    <iframe src="https://drive.google.com/file/d/1Qx8h8Xk7lofHnyGyb6IlRQefgk_TxCuQ/view?usp=sharing" width="700" height="1000" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.error("Failed to load PDF.")
