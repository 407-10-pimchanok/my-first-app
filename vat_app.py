import streamlit as st

#แสดงชื่อแอปพลิเคชั่น
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

#สร้างช่องรับข้อมูลตัวเลขราคา
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

#ตัวแปร vat คำนวณ 7%
vat = price * 0.07

#ตัวแปร net_price คำนวณราคา - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")

#แสดงจำนวน Vat
net_price = price - vat

#แสดงราคาสุทธิ
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

#สร้างเส้นกั้น
st.divider()

#แสดงข้อมูลนักเรียน
st.write("พิมพ์ชนก กาไชย เลขที่ 10 ม.4/7")
