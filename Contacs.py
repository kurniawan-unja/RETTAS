import streamlit as st

def Contacs():
    st.title('Tim Penelitian Aplikasi RETTAS')
# Membuat 2 kolom
    col1, col2, col3 = st.columns(3)

# Menampilkan konten di kolom pertama
    with col1:
        st.write("Ketua Tim Peneliti")
        #st.write("Ini adalah konten di kolom pertama.")
        st.image("jufrida.jpeg", width= 150, caption="Dra. Jufrida., M.Si")

# Menampilkan konten di kolom kedua
    with col2:
        st.write("Anggota Tim Peneliti")
        st.image("wawan.jpg",  width= 150,caption="Wawan Kurniawan, S.Si., M.Cs")

# Menampilkan konten di kolom kKetiga
    with col3:
        st.write("Anggota Tim Peneliti")
        st.image("Furqon.jpg",  width=150, caption="M. Furqon, S.Pd., M.Pd")
