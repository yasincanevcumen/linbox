# Linbox | Modern Analiz Platformu

Linbox, kullanıcıların temel ve ileri düzey matematik operasyonlarını gerçekleştirmesini sağlayan, modern ve interaktif bir web tabanlı analiz platformudur. Bu proje, Python'un güçlü hesaplama yeteneklerini, Flask ile oluşturulmuş bir web sunucusu üzerinden, dinamik ve kullanıcı dostu bir HTML/CSS/JavaScript arayüzüne sunar.
---

### ✨ **Platform Özellikleri**

* **🧠 Modüler Analiz Araçları:**
    * **Matris İşlemcisi:** Determinant, transpoze, ters matris, iz, özdeğer ve temel matris aritmetiği gibi kapsamlı operasyonlar.
    * **Türev Analizörü:** Sembolik olarak girilen fonksiyonların türevini hesaplar.
    * **İntegral Hesaplayıcı:** Fonksiyonların belirli aralıktaki belirli integralini bulur.

* **🖥️ Sade ve Fonksiyonel Tasarım:**
    * **Modüler Navigasyon:** Farklı analiz araçları arasında geçişi sağlayan, temiz ve minimalist bir sol menü.
    * **Dinamik Arayüz:** Kullanıcının seçtiği matris boyutuna ve sayısına göre anında adapte olan, akıllı giriş alanları.
    * **Duyarlı (Responsive) Yapı:** Masaüstü ve mobil cihazlarda tutarlı ve akıcı bir kullanıcı deneyimi.

* **💡 Etkileşimli Sonuç Görselleştirme:**
    * Hesaplama sonuçları, işlemin türüne (sayı, matris, dizi) göre farklı ve şık animasyonlarla sunulur. Bu, verinin daha kolay yorumlanmasını sağlar.

---

### 🛠️ **Kullanılan Teknolojiler**

* **Backend:**
    * **Python 3:** Ana programlama dili.
    * **Flask:** Hafif ve esnek web sunucusu.
    * **NumPy:** Yüksek performanslı matris hesaplamaları için.
    * **SymPy:** Sembolik matematik (türev, integral) işlemleri için.

* **Frontend:**
    * **HTML5 & CSS3:** "Apple tarzı" minimalist estetiği yansıtan, modern ve sade arayüz tasarımı.
    * **JavaScript (ES6):** Arayüz dinamizmi, modüler sayfa yönetimi ve `Fetch API` aracılığıyla sunucu ile asenkron iletişim.

---

## 🚀 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Proje Dosyalarını İndirin:**
   - Projenin tüm dosyalarını (`app.py`, `templates/` klasörü vb.) bir klasöre indirin.

**2. Sanal Ortam (Virtual Environment) Oluşturun (Önerilir):**
   - Terminali proje klasöründe açın ve aşağıdaki komutları çalıştırın:
     ```bash
     # Sanal ortamı oluştur
     python -m venv env

     # Sanal ortamı aktive et
     # Windows için:
     .\env\Scripts\activate
     # macOS / Linux için:
     source env/bin/activate
     ```

**3. Gerekli Kütüphaneleri Yükleyin:**
   - Proje için gerekli olan tüm Python kütüphanelerini `requirements.txt` dosyasını kullanarak tek komutla yükleyin:
     ```bash
     pip install -r requirements.txt
     ```
     *(Eğer requirements.txt dosyanız yoksa, şu komutları çalıştırın: `pip install Flask numpy sympy`)*

**4. Python Sunucusunu Başlatın:**
   - Her şey hazır! Aşağıdaki komutla Flask sunucusunu başlatın:
     ```bash
     python app.py
     ```
   - Terminalde sunucunun `http://127.0.0.1:5000` adresinde başladığına dair bir mesaj göreceksiniz.

**5. Tarayıcıda Açın:**
   - Web tarayıcınızı açın ve adres çubuğuna `http://127.0.0.1:5000` yazın.
   - Linbox analiz platformu artık kullanıma hazır!
