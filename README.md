# Django KİŞİSEL WEB SAYFASI

Bu proje, **Django framework** kullanarak geliştirilmiş bir **kişisel web sayfasıdır**. Sayfada **projeler listelenir, detaylar incelenir ve iletişim bilgileri gibi kısımlar bulunur**. Kullanıcılar projeleri görüntüleyebilir ve detay sayfasına geçiş yapabilir. **Admin panelinde ise yetkili kişiler, kullanıcıları yönetebilir, projeler ve kategoriler ekleyip düzenleyebilir.**

----------

## **💡 Projenin Genel Yapısı**

### **📂 1. Ana Bileşenler**

-   **Ana Sayfa (`index1.html`)**:
    
    -   Projeler listelenir.
    -   Proje detaylarına gitmek için buton bulunur.
-   **Proje Detay Sayfası (`detaylar.html`)**:
    
    -   Seçilen projenin detayları görüntülenir.
    -   "Geri Dön" butonu ile ana sayfaya geri dönülür.
-   **Statik Dosyalar (`static/`)**:
    
    -   `main.css`: Sayfanın tasarımı ve stilleri.
    -   `img/`: Proje görsellerinin saklandığı klasör.
-   **Django URL Yönlendirmeleri (`urls.py`)**:
    
    -   Ana sayfa, proje detay sayfası için URL patikaları.
    -   `NoReverseMatch` gibi hatalar giderildi.
-   **Model Yapısı (`models.py`)**:
    
    -   `Proje` modeli oluşturuldu.
    -   Proje bilgileri (**isim, açıklama, resim, tarih**) veritabanında saklanıyor.

----------

## **🔧 Kurulum & Kullanım**

### **✨ 1. Django Projesini Kurma**

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsin:

```bash
# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Veritabanını oluşturun
python manage.py migrate

# Sunucuyu başlatın
python manage.py runserver

```

### **🌟 2. Admin Panelini Kullanma**

```bash
# Admin kullanıcısı oluştur
python manage.py createsuperuser

# Admin paneline gir
http://127.0.0.1:8000/admin/

```

![Image](https://github.com/user-attachments/assets/23fc1cb1-39f3-4669-9892-4dffcfe17524)

----------

## **🔄 URL Yönlendirmeleri**

`/projeler/<id>`

Seçilen projenin detayları


----------

## **🌐 Teknolojiler & Araçlar**

-   **Python** (v3.10)
-   **Django** (v4+)
-   **HTML, CSS, Bootstrap** (Responsive tasarım)
-   **SQLite/PostgreSQL** (Veritabanı)
-   **FontAwesome** (Simge kullanımları)

----------

## **🎨 Geliştirme Süreci**

-   Django kurulumu yapıldı
-   **Projeler modeli** oluşturuldu
-   **Ana Sayfa ve Detay Sayfası** geliştirildi
-   **CSS tasarımları modernleştirildi**
-   **URL yönlendirmeleri düzeltildi**
-   **Form ekleme ve blog sayfası** (geliştirme aşamasında)

----------

## **🚀 Yapılacaklar & Geliştirme Fikirleri**

-   Projeler için **yorum ekleme** modülü ekleme
-   **İletişim formu** ekleyerek mail gönderme
-   **Blog sayfası** ekleme

----------
### MAHMUT KEREM ERDEN - k.erden03@gmail.com
