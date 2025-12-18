import streamlit as st

# ล็อก password (เปลี่ยน "1234" เป็นรหัสที่มึงอยากใช้)
password = st.text_input("ใส่รหัสเข้าเว็บ", type="password")
if password != "1234":
    st.stop()

st.title("เว็บลับของมึง")

st.write("Private ติ๊กเลือกข้อมูลแล้วกดประมวลผล")

opt1 = st.checkbox("ตัวเลือก 1")
opt2 = st.checkbox("ตัวเลือก 2")
opt3 = st.checkbox("ตัวเลือก 3")
opt4 = st.checkbox("ตัวเลือก 4")

if st.button("ประมวลผล"):
    selected = []
    if opt1: selected.append("ตัวเลือก 1")
    if opt2: selected.append("ตัวเลือก 2")
    if opt3: selected.append("ตัวเลือก 3")
    if opt4: selected.append("ตัวเลือก 4")
    
    if selected:
        st.success(f"มึงติ๊ก: {', '.join(selected)}")
        # ตรงนี้ใส่สูตรหรือ logic จริงของมึงต่อ
    else:
        st.warning("ยังไม่ได้ติ๊กอะไร")