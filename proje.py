import streamlit as st
import os

# 1. Dokümanları Okuma Fonksiyonu
def dokumanlari_oku():
    dokumanlar = {}
    # Klasördeki ders notlarını tara
    for i in range(1, 6):
        dosya_adi = f"ders_notu_{i}.txt"
        if os.path.exists(dosya_adi):
            with open(dosya_adi, "r", encoding="utf-8") as f:
                dokumanlar[dosya_adi] = f.read()
    return dokumanlar

# 2. Basit RAG Arama Algoritması
def basit_rag_sistemi(soru, dokumanlar):
    en_iyi_dokuman = None
    en_iyi_icerik = None
    en_yuksek_skor = 0
    
    # Soruyu küçük harflere çevir ve kelimelerine ayır
    soru_kelimeleri = soru.lower().split()
    
    for dosya, icerik in dokumanlar.items():
        skor = 0
        # Doküman içindeki satırları veya paragrafları tara
        satirlar = icerik.split('\n')
        for satir in satirlar:
            if not satir.strip():
                continue
            
            # Satırdaki eşleşen kelime sayısını bul
            satir_skoru = sum(1 for kelime in soru_kelimeleri if kelime in satir.lower())
            
            if satir_skoru > en_yuksek_skor:
                en_yuksek_skor = satir_skoru
                en_iyi_dokuman = dosya
                en_iyi_icerik = satir.strip()
                
    if en_yuksek_skor > 0:
        return en_iyi_dokuman, en_iyi_icerik
    else:
        return None, "İlgili bilgi dokümanlar içinde bulunamadı!"

# --- STREAMLIT WEB ARAYÜZÜ TASARIMI ---
st.set_page_config(page_title="RAG Ders Asistanı", page_icon="🤖", layout="centered")

st.title("🤖 Yapay Zekâ Destekli Ders Notu Asistanı")
st.markdown("---")
st.write("Sorunuzu aşağıdaki kutuya yazın, sistem ders notlarınızdan bulup kaynak göstersin!")

# Dokümanları arka planda yükle
notlar = dokumanlari_oku()

# Kullanıcı Soru Girişi
kullanici_sorusu = st.text_input("Sorunuzu yazın:", placeholder="Örn: RAG mimarisinin temel amacı nedir?")

if kullanici_sorusu:
    with st.spinner('Dokümanlar taranıyor...'):
        dosya, cevap = basit_rag_sistemi(kullanici_sorusu, notlar)
        
    if dosya:
        st.success(f"📌 **İlgili içerik başarıyla bulundu!**")
        st.info(f"📄 **Kaynak:** `{dosya}`")
        st.write(f"💬 **Cevap:** {cevap}")
    else:
        st.warning(f"⚠️ {cevap}")

# Alt Bilgi
st.markdown("---")
st.caption("Akademik Yapay Zekaya Giriş Bireysel Ürün Geliştirme Projesi")