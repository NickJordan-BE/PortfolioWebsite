import streamlit as st
import base64

st.title("My Resume")

with open("https://nickjordan.streamlit.app/static/NickJordanResumeML.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File   
    st.markdown(pdf_display, unsafe_allow_html=True)