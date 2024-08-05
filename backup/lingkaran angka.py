import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def tampilkan_halaman():
    if 'show_terms' not in st.session_state:
        st.session_state.show_terms = False

    # Tombol di sidebar untuk kembali ke halaman utama
    with st.sidebar:
        if st.button("Halaman Utama"):
            st.session_state.halaman = 'utama'
            st.experimental_rerun()

    # Menampilkan komponen file uploader
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    # Menambahkan tombol Syarat dan Ketentuan
    if st.button("Syarat dan Ketentuan"):
        if st.button("Tutup"):
            st.session_state.show_terms = False
        st.info("Berikut adalah syarat dan ketentuan penggunaan aplikasi:")
        st.text("1. File harus berformat CSV \n2. Untuk contoh isi file CSV seperti gambar ini :")
        st.image("E:/magang/streamlit/foto/image.png")

    # Jika file diunggah
    if uploaded_file is not None:
        # Membaca data dari file CSV yang diunggah
        data = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah dan dibaca")

        # Ekstraksi nama kolom pertama
        kolom_pertama = data.columns[0]
        st.write(f"Kolom pertama: {kolom_pertama}")

        # Ekstraksi data dari kolom pertama
        label_pertama = data[kolom_pertama]
        
        # Menampilkan daftar tahun yang tersedia
        years = data.columns[1:]  # Mengambil semua kolom kecuali kolom pertama
        selected_year = st.selectbox("Pilih tahun:", years)

        # Ekstraksi jumlah penduduk untuk tahun yang dipilih
        jumlah = data[selected_year]

        # Fungsi untuk format angka pada sumbu y
        def absolute_value(val):
            a  = int(round(val/100.*sum(jumlah), 0))
            return '{:d}'.format(a)

        # Membuat diagram lingkaran
        fig, ax = plt.subplots(figsize=(10, 11))
        ax.pie(jumlah, labels=label_pertama, autopct=absolute_value, startangle=140)

        # Menambahkan jumlah total penduduk di pojok kanan atas
        total = sum(jumlah)
        ax.text(1.5, 1.5, f'Total: {total}', horizontalalignment='right', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

        ax.set_title(f'Hasil Diagram Lingkaran Tahun {selected_year}')
        ax.axis('equal')

        # Menampilkan diagram menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")
