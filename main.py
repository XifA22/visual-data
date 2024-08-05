
import streamlit as st

# Fungsi untuk halaman utama
def halaman_utama():
    st.title("Selamat Datang \n Silahkan pilih diagram yang ingin digunakan")
    if st.button("Diagram Lingkaran"):
        st.session_state['halaman'] = 'Diagram Lingkaran'
    if st.button("Diagram Batang"):
        st.session_state['halaman'] = 'Diagram Batang'
    if st.button("Diagram Garis"):
        st.session_state['halaman'] = 'Diagram Garis'

# Menentukan halaman yang akan ditampilkan berdasarkan status aplikasi
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'utama'

if st.session_state['halaman'] == 'utama':
    halaman_utama()
elif st.session_state['halaman'] == 'Diagram Lingkaran':
    import lingkaran
    lingkaran.tampilkan_halaman()
elif st.session_state['halaman'] == 'Diagram Batang':
    import batang
    batang.tampilkan_halaman()
elif st.session_state['halaman'] == 'Diagram Garis':
    import garis
    garis.tampilkan_halaman()
