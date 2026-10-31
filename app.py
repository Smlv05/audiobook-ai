import streamlit as st

st.set_page_config(page_title="AI Audiobook Generator", layout="centered")

st.title("AI Audiobook Generator")
st.write("Upload an EPUB book to convert it into an audiobook.")

uploaded = st.file_uploader("EPUB file", type=["epub"])

if uploaded is not None:
    st.success(f"Loaded: {uploaded.name} ({uploaded.size / 1024:.0f} KB)")
    st.info("Processing pipeline is not implemented yet.")