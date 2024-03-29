import streamlit as st
import math

st.title('TitriPro')

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
    
    massa = st.number_input('Masukkan nilai massa (mg)',format="%.1f",value=default_value)
    volume = st.number_input('Masukkan nilai volume (mL)',format="%.2f",value=default_value)
    BE1 = st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f",value=default_value)
    FP1 = st.number_input('Masukkan nilai F Pengali',format="%.0f",value=default_value)

    tombol = st.button('Hitung nilai normalitasnya')

    nilai_normalitas1=massa/(BE1*volume*FP1)
    if tombol:
        nilai_normalitas = massa/(BE1*volume*FP1)
        st.success(f'Nilai normalitas adalah {nilai_normalitas:.4f}N')

    Vtitran = st.number_input('Masukkan nilai volume titran (mL)',value=default_value)
    Ntitran = st.number_input('Masukkan nilai normalitas titran (N)',format='%.4f', value=(nilai_normalitas1))
    BE2 = st.number_input('Masukkan nilai BEnya (mg/mgrek)',format="%.1f",value=default_value)
    FP2 = st.number_input('Masukkan nilai F Pengalinya',format="%.0f",value=default_value)
    Vtitrat = st.number_input('Masukkan nilai volume titrat (mL)',format="%.2f",value=default_value)
    gtitrat = st.number_input('Masukkan nilai massa (g)', format='%.4f',value=default_value )

    tombol1 = st.button('Hitung nilai kadarnya (b/v)')

    if tombol1:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
        st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}%(b/v)')   
        
    tombol2=st.button('Hitung nilai kadarnya (b/b)')
    if tombol2:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/gtitrat
        st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}%(b/b)')   

with tab2:
    
    st.title("Kalkulator pH Larutan")
    default_value = 1.0000000000
    
    jenis_larutan = st.radio("Jenis larutan :", ["Asam", "Basa"])

    if jenis_larutan == "Asam":
        konsentrasi_hidrogen = st.number_input("Masukkan konsentrasi ion H+ (mol/L):", format='%.10f', value=default_value,)
        pH = -math.log10(konsentrasi_hidrogen)
        st.write(f"pH larutan: {pH:.2f}",)     
    
    elif jenis_larutan == "Basa":
        konsentrasi_hidroksida = st.number_input("Masukkan konsentrasi ion OH- (mol/L):", format='%.10f', value=default_value,)
        pOH = -math.log10(konsentrasi_hidroksida)
        pH = 14 - pOH
        st.write(f"pH larutan: {pH:.2f}")
          
    

