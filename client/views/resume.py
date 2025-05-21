import streamlit as st

st.title("My Resume")

file_id = "1Qx8h8Xk7lofHnyGyb6IlRQefgk_TxCuQ"  # Replace with your actual file ID

embed_url = f"https://drive.google.com/file/d/{file_id}/preview"

st.markdown(
    f'<iframe src="{embed_url}" width="700" height="1000" allow="autoplay"></iframe>',
    unsafe_allow_html=True
)

