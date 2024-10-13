import streamlit as st



# Membuat 2 kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom 1")
    st.write("Ini adalah konten di kolom pertama.")
    st.image("https://via.placeholder.com/150", caption="Gambar di kolom 1")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom 2")
    st.write("Ini adalah konten di kolom kedua.")
    st.image("https://via.placeholder.com/150", caption="Gambar di kolom 2")

