import os

def dokumanlari_oku():
    veriler = {}
    for dosya_adi in os.listdir('.'):
        if dosya_adi.endswith('.txt') and dosya_adi.startswith('ders_notu_'):
            with open(dosya_adi, 'r', encoding='utf-8') as f:
                veriler[dosya_adi] = f.read()
    return veriler

def basit_rag_sistemi(soru, dokumanlar):
    en_iyi_dokuman = None
    en_iyi_icerik = "Maalesef bu konuyla ilgili ders notlarinda bilgi bulamadim."
    en_yuksek_skor = 0
    
    soru_kelimeleri = soru.lower().split()
    
    for dosya, icerik in dokumanlar.items():
        skor = 0
        alt_icerik = icerik.lower()
        for kelime in soru_kelimeleri:
            if kelime in alt_icerik:
                skor += 1
                
        if skor > en_yuksek_skor:
            en_yuksek_skor = skor
            en_iyi_dokuman = dosya
            en_iyi_icerik = icerik
            
    return en_iyi_dokuman, en_iyi_icerik

print("--- Basit Ders Notu Yapay Zeka Sistemine Hos Geldiniz ---")
notlar = dokumanlari_oku()

while True:
    kullanici_sorusu = input("\nSorunuzu yazin (Cikmak icin 'exit' yazin): ")
    if kullanici_sorusu.lower() == 'exit':
        print("Sistem kapatiliyor...")
        break
        
    dosya, cevap = basit_rag_sistemi(kullanici_sorusu, notlar)
    
    if dosya:
        print(f"\n[Sistem]: {dosya} icinde ilgili bilgiler bulundu!")
        print(f"[Cevap]: {cevap}")
    else:
        print(f"\n[Sistem]: {cevap}")