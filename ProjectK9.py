import streamlit as st
import math

st.title('Aplikasi perhitungan normalitas dan persentase kadar')

st.write('Oleh Kelompok 9')
st.write('Ali Akbar Mustaqim (2219030)')
st.write('Jecly Nur Fauzan (2219088)')
st.write('Mafhum Shihab Khalwany (2219102)')
st.write('Muhammad Dzaki Pratama Putra (2219114)')
st.write('Rai Aria Yudistira (2219148)')


tab1, tab2, = st.tabs(["Perhitungan Normalitas dan Kadar", "Perhitungan pH",])

with tab1:
    
    st.title("Kalkulator Normalitas dan Kadar")
    default_value = 1.0000
    min_value = 0.0000
    max_value = 9999.0000
    
    massa = st.number_input('Masukkan nilai massa (mg)',format="%.4f",value=default_value,)
    volume = st.number_input('Masukkan nilai volume (mL)',format="%.2f",value=default_value,)
    BE1 = st.number_input('Masukkan nilai BE',format="%.1f",value=default_value,)
    FP1 = st.number_input('Masukkan nilai F Pengali',format="%.0f",value=default_value,)

    tombol = st.button('Hitung nilai normalitasnya')

    nilai_normalitas1=massa/(BE1*volume*FP1)
    if tombol:
        nilai_normalitas = massa/(BE1*volume*FP1)
        st.success(f'Nilai normalitas adalah {nilai_normalitas}')


    Vtitran = st.number_input('Masukkan nilai volume titran (mL)')
    Ntitran = st.number_input('Masukkan nilai normalitas titran (N)',format='%.4f', value=(nilai_normalitas1))
    BE2 = st.number_input('Masukkan nilai BEnya',format="%.1f")
    FP2 = st.number_input('Masukkan nilai F Pengalinya',format="%.0f")
    Vtitrat = st.number_input('Masukkan nilai volume titrat (mL)',format="%.0f")

    tombol = st.button('Hitung nilai kadarnya')

    if tombol:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
        st.success(f'Persentase kadarnya adalah {nilai_kadar}%')   

with tab2:
    
    st.title("Kalkulator pH Larutan")
    default_value = 1.0000
    

    jenis_larutan = st.radio("Jenis larutan yang diukur:", ["Asam", "Basa"])

    if jenis_larutan == "Asam":
        st.write("Larutan asam: HCl, H2SO4, HNO3, dll.")
        # Input konsentrasi ion hidrogen (H+) dalam mol/L
        c_H = st.number_input("Masukkan konsentrasi ion H+ (mol/L):", format="%.10f", value=default_value,)
        # Menghitung pH larutan
        pH = -math.log10(c_H)
        st.write(f"pH larutan: {pH:.2f}",)
     
    
    elif jenis_larutan == "Basa":
        st.write("Larutan basa: NaOH, KOH, Ca(OH)2, dll.")
        # Input konsentrasi ion hidroksida (OH-) dalam mol/L
        c_OH = st.number_input("Masukkan konsentrasi ion OH- (mol/L):", format="%.10f", value=default_value,)
        # Menghitung pOH larutan
        pOH = -math.log10(c_OH)
        # Menghitung pH larutan
        pH = 14 - pOH
        st.write(f"pH larutan: {pH:.2f}")
          
    

