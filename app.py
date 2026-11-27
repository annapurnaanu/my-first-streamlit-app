import streamlit as st


st.set_page_config(page_title="My First App", page_icon="👋", layout="centered")

st.title("My first web app")
st.write("A tiny app built with Streamlit.")

name = st.text_input("What's your name?")

if st.button("Say hello", type="primary"):
    if name.strip():
        st.success(f"Hello, {name.strip()}!")
    else:
        st.warning("Type your name above first.")
