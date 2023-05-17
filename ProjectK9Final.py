import streamlit as st
import math

st.title('TitriPro')
st.write('---------------------------------------------------------------------------------')
st.write('Oleh Kelompok 9')
st.write('Ali Akbar Mustaqim (2219030)')
st.write('Jecly Nur Fauzan (2219088)')
st.write('Mafhum Shihab Khalwany (2219102)')
st.write('Muhammad Dzaki Pratama Putra (2219114)')
st.write('Rai Aria Yudistira (2219148)')

tab1, tab2, = st.tabs(["Home", "Perhitungan",])

with tab1:
    

    st.write('TitriPro adalah sebuah aplikasi yang dibuat untuk mempermudahan analis kimia dalam perhitungan saat titrasi dalam menentukan Normalitas dan Kadar, sementara titrasi menurut pengertiannya adalah (cara analisa tentang pengukuran jumlah larutan yang dibutuhkan untuk bereaksi secara tepat dengan zat yang terdapat dalam larutan lain).')
    st.write('Pada praktiknya kita akan menentukan Normalitas suatu larutan standar sekunder(HCl,NaOH, KMnO4, Tio, dan EDTA) dengan di titrasi dengan larutan standar primer(Asam Oksalat, Boraks, Kalium Dikromat,dan Kalsium Karbonat), setelah mendapatkan Normalitas suatu larutan standar sekunder, maka normalitas larutan tersebut dapat digunakan untuk menghitung kadar larutan dalam suatu sampel.')
    
    
with tab2:
    option=st.selectbox(
    'Silahkan pilih perhitungan yang ingin dicari',
    ('Menentukan normalitas dan kadar dalam larutan','Perhitungan pH'))
    
    
    if option=='Menentukan normalitas dan kadar dalam larutan':
        st.header('Menghitung Normalitas')
        default_value = 1.0000000000
    
    
        massa = st.number_input('Masukkan nilai massa (mg)',format="%.1f",value=default_value)
        volume = st.number_input('Masukkan nilai volume (mL)',format="%.2f",value=default_value)
        BE1 = st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f",value=default_value)
        FP1 = st.number_input('Masukkan nilai F Pengali',format="%.0f",value=default_value)

        tombol = st.button('Hitung nilai normalitasnya')

        nilai_normalitas1=massa/(BE1*volume*FP1)
        if tombol:
            nilai_normalitas = massa/(BE1*volume*FP1)
            st.success(f'Nilai normalitas adalah {nilai_normalitas:.4f}N')
    
    
        st.header('Menghitung Kadar Dalam Larutan')
        
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
        
        
        
    elif option=='Perhitungan pH':
        default_value = 1.0000000000
    
        jenis_larutan = st.radio("Jenis larutan :", ["Asam", "Basa"])

        if jenis_larutan == "Asam":
            st.write(f'Contoh Larutan Asam : HCl, H2SO4, HNO3, HCN, HF, Dll')
        
            konsentrasi_hidrogen = st.number_input("Masukkan konsentrasi ion H+ (mol/L):", format='%.10f', value=default_value,)
            pH = -math.log10(konsentrasi_hidrogen)
            if pH > 14 :
                st.error('------------------------------error | please input number of consentration correct------------------------------')
                st.stop()
            if pH < 1:
                st.error('------------------------------error | please input number of consentration correct------------------------------')
                st.stop()
            else :
                st.write(f"pH larutan: {pH:.2f}")
        
        
        elif jenis_larutan == "Basa":
            st.write(f'Contoh Larutan Basa : NaOH, KOH, Mg(OH)2, Ba(OH)2, Dll')
            
            konsentrasi_hidroksida = st.number_input("Masukkan konsentrasi ion OH- (mol/L):", format='%.10f', value=default_value,)
            pOH = -math.log10(konsentrasi_hidroksida)
            pH = 14 - pOH
            if pH > 14 :
                st.error('------------------------------error | please input number of consentration correct------------------------------')
                st.stop()
            if pH < 1:
                st.error('------------------------------error | please input number of consentration correct------------------------------')
                st.stop()
            else :
                st.write(f"pH larutan: {pH:.2f}")