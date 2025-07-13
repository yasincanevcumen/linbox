# Linbox | Matris İşlemcisi

Linbox, kullanıcıların temel ve ileri düzey matris operasyonlarını gerçekleştirmesini sağlayan, modern ve interaktif bir web tabanlı analiz platformudur. Bu proje, Python'un güçlü hesaplama yeteneklerini, Flask ile oluşturulmuş bir web sunucusu üzerinden, dinamik ve kullanıcı dostu bir HTML/CSS/JavaScript arayüzüne sunar.

## ✨ Özellikler

- **Tek Matrisli Operasyonlar:** Determinant, Transpoze, Ters Matris, İz (Trace) ve Özdeğer (Eigenvalue) hesaplama.
- **İki Matrisli Operasyonlar:** Toplama, Çıkarma ve Matris Çarpımı.
- **Dinamik Arayüz:** Kullanıcının seçtiği matris adedine ve boyutuna göre anında güncellenen giriş alanları.
- **Animasyonlu Sonuçlar:** Hesaplama sonuçları, işlemin türüne (sayı, matris, dizi) göre farklı ve şık animasyonlarla görselleştirilir.
- **Modern ve Kullanıcı Dostu Tasarım:** Aydınlık, yumuşak tonlar ve oval hatlarla tasarlanmış, göz yormayan bir kullanıcı deneyimi.
- **Genişletilebilir Menü:** Platformun gelecekte "Kavramlar", "Tarihçe" gibi yeni matematiksel içeriklerle zenginleştirilmesine olanak tanıyan menü yapısı.

---

## 🛠️ Teknoloji Stack'i

- **Backend:**
    - **Python 3:** Ana programlama dili.
    - **Flask:** Hafif ve hızlı web sunucusu oluşturmak için.
    - **NumPy:** Tüm karmaşık matris hesaplamaları için.
    - **Flask-Cors:** Frontend ve backend arasındaki iletişimi sağlamak için.
- **Frontend:**
    - **HTML5:** Sayfanın yapısı.
    - **CSS3:** Modern ve şık tasarım (değişkenler, gradyanlar, animasyonlar).
    - **JavaScript (ES6):** Arayüz dinamizmi ve sunucu ile iletişim (API istekleri).

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
   - Proje için gerekli olan Python kütüphanelerini `requirements.txt` dosyasını kullanarak tek komutla yükleyin:
     ```bash
     pip install -r requirements.txt
     ```

**4. Python Sunucusunu Başlatın:**
   - Her şey hazır! Aşağıdaki komutla Flask sunucusunu başlatın:
     ```bash
     python app.py
     ```
   - Terminalde sunucunun `http://127.0.0.1:5000` adresinde başladığına dair bir mesaj göreceksiniz.

**5. Tarayıcıda Açın:**
   - Web tarayıcınızı açın ve adres çubuğuna `http://127.0.0.1:5000` yazın.
   - Linbox matris işlemcisi artık kullanıma hazır!
