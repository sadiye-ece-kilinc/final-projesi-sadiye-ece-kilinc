#  Yapay Zekâ Destekli Akıllı Ders Notu Arama Asistanı (v1.0.0 End-to-End Enterprise Release)

##  1. Proje Hakkında Genel Bakış ve Yönetici Özeti
Bu proje, üniversite ve akademi öğrencilerinin vizeler ile finaller öncesinde karmaşık, yüzlerce sayfalık ders notları, slayd çıktıları ve PDF dokümanları arasında aradıkları nokta atışı bilgilere ulaşamaması problemine kesin bir çözüm üretmek üzere tasarlanmıştır. 

Klasik yapay zekâ sohbet robotları (ChatGPT, Gemini vb.) doğrudan kendilerine yüklenmeyen veriler hakkında konuşurken dış dünyadan uydurma bilgiler üretebilmekte ve akademik süreçlerde öğrencileri yanlış yönlendirebilmektedir (Halüsinasyon Problemi). Bu proje, bu büyük riskin önüne geçebilmek amacıyla **Retrieval-Augmented Generation (RAG)** mimarisinin yerel (local) bir simülasyonunu ayağa kaldırmaktadır. 

Sistem, dış dünyayla tüm bağlarını kopararak sadece geliştiricinin veya öğrencinin sisteme beslediği **5 farklı ders notu havuzunu (`ders_notu_1.txt` ... `ders_notu_5.txt`)** baz alır. Kullanıcı bir sorgu girdiğinde, sistem ilgili dokümanları satır satır tarar, anlamsal bütünlüğü koruyarak veriyi ekrana basar. Eğer bilgi kaynak dokümanlarda yoksa uydurma bilgi üretmek yerine güvenli tarafta kalıp kullanıcıyı uyarır.

---

##  2. Detaylı Proje Dosya Yapısı ve Dizin Ağacı Açıklamaları

Proje dizin mimarisi, modüler yazılım geliştirme prensiplerine ve temiz kod (clean code) standartlarına uygun olarak tasarlanmıştır. Dizin yapısının detaylı görünümü ve her bir dosyanın üstlendiği görev şu şekildedir:

```text
final-projesi/
│
├── ders_notu_1.txt       # RAG (Retrieval-Augmented Generation) Nedir?, Temel Kavramlar Dokümanı
├── ders_notu_2.txt       # Metinlerin Vektörleştirilmesi (Embedding) ve Temsil Edilmesi Ders Notu
├── ders_notu_3.txt       # Vektör Benzerliği, Cosine Similarity ve Skorlama Mantığı Ders Notu
├── ders_notu_4.txt       # Chunking (Büyük Metinleri Parçalara Bölme) Stratejileri Ders Notu
├── ders_notu_5.txt       # Veri Yapıları, Graflar (Graphs) ve Ağaçlar (Trees) Temel Ders Notu
│
├── proje.py              # Streamlit Web Sunucu Kodları ve Arama Motoru İş Mantığı Ana Kaynak Dosyası
├── PROJE-ONERISI.md      # Dönem Başında Hoca Tarafından Onaylanan İlk Taslak Öneri Metni
└── README.md             # Projenin Tüm Detaylarını Barındıran Ana Kılavuz Dosyası (Bu Dosya)
