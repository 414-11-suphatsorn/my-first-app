import streamlit as st
st.title("แอปพลิเคเชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bn_year=st.number_input("กรอกปี พ.ศ. เป็น ค. ศ.",value=2569)
ce_year=bn_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
