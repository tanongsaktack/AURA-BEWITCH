import streamlit as st

password = st.text_input("รหัสเข้าเว็บ", type="password")
if password != "1234":  # เปลี่ยน 1234 เป็นรหัสจริงของมึง
    st.stop()

st.title("เว็บลับของมึง")

opt1 = st.checkbox("ติ๊ก 1")
opt2 = st.checkbox("ติ๊ก 2")
opt3 = st.checkbox("ติ๊ก 3")
opt4 = st.checkbox("ติ๊ก 4")

if st.button("ประมวลผล"):
    selected = []
    if opt1: selected.append("ติ๊ก 1")
    if opt2: selected.append("ติ๊ก 2")
    if opt3: selected.append("ติ๊ก 3")
    if opt4: selected.append("ติ๊ก 4")
    
    if selected:
        st.success(f"มึงติ๊ก: {', '.join(selected)}")
    else:
        st.warning("ยังไม่ได้ติ๊กอะไร")