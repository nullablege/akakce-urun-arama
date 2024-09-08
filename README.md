Akakçe Ürün Fiyat Karşılaştırma Botu
Bu Python script'i, Selenium kütüphanesini kullanarak Akakçe web sitesinde ürün araması yapar ve bulunan ürünlerin farklı satıcılar arasındaki fiyat farklarını karşılaştırır. Büyük yüzdelik fark bulunan ürünleri kaydederek kullanıcıya sunar.

Özellikler
Kullanıcı tarafından girilen ürün adı ile Akakçe'de arama yapar.
Arama sonuçları sayfasındaki tüm ürünleri dolaşır.
Ürünlerin birden fazla satıcıdan listelenen fiyatlarını karşılaştırır.
Yüzde 30 ve üzeri fark tespit edilirse, ürün bilgilerini ve farkı dosyaya yazar.
Ürün bilgilerini ve fiyatlarını dosyaya kaydeder.

Gereksinimler
Python 3.x
Selenium kütüphanesi
Chrome WebDriver
WebDriver Manager

Python Paketleri:
pip install selenium webdriver-manager

Kurulum ve Kullanım
Bu projeyi bilgisayarınıza klonlayın veya indirin.
Gerekli kütüphaneleri yüklemek için terminal/komut satırından şu komutu çalıştırın:
pip install selenium webdriver-manager
Python script'ini çalıştırın:
python akakce.py
Script çalıştıktan sonra sizden aramak istediğiniz ürünün adını girmeniz istenecektir.
Script, ürünlerin sayfalarını dolaşarak fiyat bilgilerini toplayacak ve büyük fiyat farklarını akakce.txt dosyasına yazacaktır.

Çıktılar
Ürün adı, satıcıya ait fiyat bilgileri ve varsa fiyat farkı yüzde cinsinden akakce.txt dosyasına kaydedilir.
Arama sonuçları ayrıca aramaSonuclari.txt dosyasına yazılır.

Kodda Kullanılan Önemli Fonksiyonlar
yuzdelik_fark(sayi1, sayi2): İki fiyat arasındaki yüzdelik farkı hesaplar.
WebDriverWait: Sayfa yavaş yüklendiğinde, elementlerin beklenmesi için kullanılır.
element_to_be_clickable ve element_to_be_located: Sayfa yükleme işlemlerinde elementlerin hazır olmasını kontrol eder.
