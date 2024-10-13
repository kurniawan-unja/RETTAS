import streamlit as st
from Recommendation import Recommendation
from Contacs import Contacs

# Konfigurasi halaman
st.set_page_config(
    page_title="ProjectP5 App",
    #page_icon="Logo_Universitas_Jambi-removebg-preview.png"  # Uncomment jika Anda memiliki ikon
)
st.sidebar.image("Logo_Universitas_Jambi-removebg-preview.png", width= 150,caption="Universitas Jambi")
# Sidebar navigation
st.sidebar.title("Home")
pilihan = st.sidebar.selectbox("Pilih Halaman", ("Dashboard", "Recommendation", "Contacts"))



# CSS untuk background
page_bg_img = '''
<style>
body {
    background-color: lightblue;
    color: black;
}
</style>
'''

# Display the selected page
if pilihan == "Dashboard":
    st.title("Recommended Teacher Tool Assistant System (RETTAS) ")
    st.write("Sistem RETTAS digunakan untuk merekomendasikan kepada guru sebagai penentuan tema Project "
             "Penguatan Profil Pancasila (P5) di Sekolah")
    # Menampilkan gambar dari file lokal
    st.image("jambi.jpg", caption="Gentala Arasy", use_column_width=True)
elif pilihan == "Recommendation":
    Recommendation()
elif pilihan == "Contacts":
    Contacs()

# Footer di sidebar
#st.sidebar.success("Pilih halaman di atas.")
