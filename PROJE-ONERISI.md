# PROJE ÖNERİSİ

## 1. Seçilen Görev Numarası
SEÇENEK 1 - RAG Tabanlı Uzman Bilgi Asistanı

## 2. Ürünün Adı
EduGuide-DS: Veri Yapıları Dersi Akıllı Öğrenme ve Kaynak Asistanı

## 3. Çözülecek Problem
Bilgisayar ve Yazılım Mühendisliği öğrencilerinin en çok zorlandığı derslerin başında "Veri Yapıları (Data Structures)" gelmektedir. Öğrenciler ders notları, kod örnekleri, ağaçlar (trees), bağlı listeler (linked lists) gibi soyut kavramlar arasında kaybolmakta, sınav dönemlerinde hoca notlarından hızlıca doğru bilgiye ve ilgili Java koduna ulaşmakta güçlük çekmektedir. Mevcut genel yapay zekâ araçları (ChatGPT vb.) doğrudan dersin kendi müfredatına ve hocanın anlatım tarzına göre özelleştirilmiş cevaplar verememektedir. Bu proje, öğrencinin doğrudan kendi ders dokümanları üzerinden, doğrulanmış ve kaynak gösterilmiş bilgiye ulaşmasını sağlayarak bu problemi çözer.

## 4. Hedef Kullanıcı
Üniversitelerin Bilgisayar/Yazılım Mühendisliği bölümlerinde okuyan, "Veri Yapıları ve Algoritmalar" dersini alan öğrenciler ve dersi yürüten akademisyenler.

## 5. Kullanılacak Veri veya Bilgi Kaynakları
Veri yapıları müfredatına uygun olarak hazırlanmış en az 5 farklı akademik doküman ve ders materyali kullanılacaktır:
1. Ders Notu 1: Giriş ve Algoritma Analizi (Big-O Notasyonu)
2. Ders Notu 2: Bağlı Listeler (Linked Lists) ve ArrayList Yapısı
3. Ders Notu 3: Yığın (Stack) ve Kuyruk (Queue) Yapıları
4. Ders Notu 4: Ağaç Yapıları (Trees) ve İkili Arama Ağaçları (BST)
5. Ders Notu 5: Java ile Veri Yapıları Uygulamaları, Override Fonksiyonları ve Sınav İpuçları

## 6. Kullanılması Planlanan Teknolojiler
- **Dil:** Python 3.10+
- **Arayüz:** Streamlit (Kullanıcı dostu web arayüzü için)
- **RAG & LLM Çerçevesi:** LangChain
- **Vektör Veritabanı:** FAISS veya Chroma (Yerel ve hızlı çalışan vektör veri tabanı)
- **Gömme (Embedding) Modeli:** Hugging Face (sentence-transformers)
- **Dil Modeli:** OpenAI GPT-3.5-Turbo veya Groq API (Llama 3)

## 7. Beklenen Ürün Çıktısı
Kullanıcının veri yapıları dersiyle ilgili (Örn: "İkili arama ağacına eleman ekleme kodu nasıldır?") soru sorabildiği, sistemin ilgili bilgiyi bularak getirdiği, cevabın altında tam olarak hangi dokümana dayandığını (Kaynak Gösterimi) listelediği çalışan bir web uygulaması.

## 8. Ürünün Diğer Çalışmalardan Ayrılan Yönü
Genel yapay zekâ botlarının aksine, dış kaynaklardan ezbere bilgi getirmek yerine tamamen hocanın veya dersin kaynak dokümanlarına sadık kalır. İnternetteki bilgi kirliliğini önler ve doğrudan Java diliyle yapılandırılmış müfredat odağında çalışır. Kaynakta olmayan bir soru sorulduğunda halüsinasyon görmek yerine "Bu bilgi ders kaynaklarında bulunamadı" uyarısı verir.
