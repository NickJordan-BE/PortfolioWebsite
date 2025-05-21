import streamlit as st
import base64
import requests

st.title("My Resume")


# Use iframe instead of embed
pdf_display = f"""
<iframe src="https://drive.google.com/file/d/1Qx8h8Xk7lofHnyGyb6IlRQefgk_TxCuQ/view?usp=sharing" width="700" height="1000" type="application/pdf"></iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)
