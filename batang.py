import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def tampilkan_halaman():

    # Tombol di sidebar untuk kembali ke halaman utama
    with st.sidebar:
        if st.button("Halaman Utama"):
            st.session_state.halaman = 'utama'
            st.experimental_rerun()

    # Menampilkan komponen file uploader
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    # Menambahkan tombol Syarat dan Ketentuan
    if st.button("Panduan Penggunaan"):
        if st.button("Tutup"):
            st.session_state.show_terms = False
        st.info("Berikut cara penggunaan aplikasi:")
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
        opsi = data.columns[1:]  # Mengambil semua kolom kecuali kolom pertama
        selected_opsi = st.selectbox("Pilih Opsi:", opsi)

        # Ekstraksi jumlah penduduk untuk tahun yang dipilih
        jumlah = data[selected_opsi]

        # Membuat diagram batang vertikal
        fig, ax = plt.subplots(figsize=(30, 15))
        bars = ax.bar(label_pertama, jumlah, color='skyblue')

        # Menambahkan judul dan label
        ax.set_title(f'Hasil Diagram Batang {selected_opsi}')
        ax.set_xlabel(kolom_pertama)

        # Menambahkan grid
        ax.grid(True, linestyle='--', alpha=0.7)

        # Menambahkan angka detail di atas batang
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:,.0f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

        # Menampilkan diagram batang vertikal menggunakan Streamlit
        st.pyplot(fig)

        # Membuat diagram batang horizontal
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(label_pertama, jumlah, color='lightgreen')

        # Menambahkan judul dan label
        ax.set_title(f'Hasil Diagram Batang {selected_opsi}')
        ax.set_ylabel(kolom_pertama)

        # Menambahkan grid
        ax.grid(True, linestyle='--', alpha=0.7)

        # Menambahkan angka detail di samping batang
        for bar in bars:
            width = bar.get_width()
            ax.annotate(f'{width:,.0f}',
                        xy=(width, bar.get_y() + bar.get_height() / 2),
                        xytext=(3, 0),  # 3 points horizontal offset
                        textcoords="offset points",
                        ha='left', va='center')

        # Menampilkan diagram batang horizontal menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")
