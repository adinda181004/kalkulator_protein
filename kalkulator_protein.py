import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kadar Protein - Metode Kjeldahl")

# Input data
volume_titran = st.number_input("Masukkan volume titran (mL)", min_value=0.0, step=0.1, format="%.1f")
normalitas_titran = st.number_input("Masukkan normalitas titran (N)", min_value=0.0, step=0.01, format="%.2f")
berat_sampel = st.number_input("Masukkan berat sampel (gram)", min_value=0.0, step=0.1, format="%.1f")
faktor_konversi = st.number_input("Masukkan faktor konversi (biasanya 6,25)", min_value=0.0, value=6.25, step=0.25, format="%.2f")

# Tombol untuk menghitung
if st.button("Hitung Kadar Protein"):
    # Hitung kadar protein menggunakan metode Kjeldahl
    massa_nitrogen = (volume_titran * normalitas_titran * 14.0) / berat_sampel
    kadar_protein = massa_nitrogen * faktor_konversi
    
    # Tampilkan hasil
    st.success(f"Kadar protein adalah {kadar_protein:.2f} gram protein per 100 gram sampel.")