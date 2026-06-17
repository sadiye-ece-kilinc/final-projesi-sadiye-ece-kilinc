import streamlit as st
import os

def dokumanlari_oku():
    dokumanlar = {}
    for i in range(1, 6):
        dosya_adi = f"ders_notu_{i}.txt"
        if os.path.exists(dosya_adi):
            with open(dosya_adi, "r", encoding="utf-8") as f:
                dokumanlar[dosya_adi] = f.read()
    return dokumanlar

def basit_rag_sistemi(soru, dokumanlar):
    en_iyi_dokuman = None
    en_iyi_icerik = None
    en_yuksek_skor = 0
    
    soru_kelimeleri = soru.lower().split()
    
    for dosya, icerik in dokumanlar.items():
        satirlar = icerik.split('\n')
        
        for idx, satir in enumerate(satirlar):
            if not satir.strip():
                continue
            
            satir_skoru = sum(1 for kelime in soru_kelimeleri if kelime in satir.lower())
            
            if satir_skoru > en_yuksek_skor:
                en_yuksek_skor = satir_skoru
                en_iyi_dokuman = dosya
                
                cevap_blok = satirlar[idx:idx+4]
                en_iyi_icerik = "\n".join([s.strip() for s in cevap_blok if s.strip()])
                
    if en_yuksek_skor > 0:
        return en_iyi_dokuman, en_iyi_icerik
    else:
        return None, "İlgili bilgi dokümanlar içinde bulunamadı!"

st.set_page_config(page_title="RAG Ders Asistanı", page_icon="🤖", layout="centered")

st.title("🤖 Yapay Zekâ Destekli Ders Notu Asistanı")
st.markdown("---")
st.write("Sorunuzu aşağıdaki kutuya yazın, sistem ders notlarınızdan bulup kaynak göstersin!")

notlar = dokumanlari_oku()

kullanici_sorusu = st.text_input("Sorunuzu yazın:", placeholder="Örn: RAG mimarisinin temel amacı nedir?")

if kullanici_sorusu:
    with st.spinner('Dokümanlar taranıyor...'):
        dosya, cevap = basit_rag_sistemi(kullanici_sorusu, notlar)
        
    if dosya:
        st.success(f"📌 **İlgili içerik başarıyla bulundu!**")
        st.info(f"📄 **Kaynak:** `{dosya}`")
        st.markdown("**💬 Cevap ve Detaylar:**")
        st.info(cevap)
    else:
        st.warning(f"⚠️ {cevap}")

st.markdown("---")
st.caption("Akademik Yapay Zekaya Giriş Bireysel Ürün Geliştirme Projesi")