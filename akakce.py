from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def yuzdelik_fark(sayi1, sayi2):
    ortalama = (sayi1 + sayi2) / 2.0
    fark = abs(sayi1 - sayi2)
    yuzdelik_fark = (fark / ortalama) * 100
    return yuzdelik_fark

options = Options()
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-errors")
options.add_argument("window-size=1920x1080")  

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.get("https://www.akakce.com/")
driver.maximize_window()
arama = driver.find_element(By.ID,"q")

try:
    arama = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.ID,"q"))
    )
except Exception as e:
    print("Arama bulunamadı:", e)

aranacak = input("Aranacak Olan Urunun Adını Giriniz : ")
arama.send_keys(aranacak)
time.sleep(1)
arama.send_keys(Keys.RETURN)
sayfaSayisi = driver.find_element(By.CSS_SELECTOR,"body > div.rw_v8.search_v8 > p.pager_v8.wbb_v8 > i")
sayfaSayisi = str(sayfaSayisi.text)
sayfaSayisi = sayfaSayisi.split('/')
sayfaSayisi = sayfaSayisi[1]
sayfaSayisi = int(sayfaSayisi)
print(f"Arama sonucunda {sayfaSayisi} Adet Sayfa listelenecektir. İşleminizin Sona Ermesi Minimum {sayfaSayisi*4} Saniye Sürecektir.")
sayac = 1
with open("aramaSonuclari.txt","a",encoding="utf-8") as file:
    file.write(f"{aranacak} Kelimesi için Sonuçlar : \n")
for i in range(1,sayfaSayisi):
    print(f"------{i}.Sayfa------")
    while True:
        try:
            urun = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,f"#APL > li:nth-child({sayac}) > a"))
                )
            print(f"\n\n{urun.find_element(By.TAG_NAME,'h3').text}")
            print(f"Link : {urun.get_attribute("href")}")
            try:
                fiyat1_element = driver.find_element(By.CSS_SELECTOR, f"#APL > li:nth-child({sayac}) > div > a:nth-child(1) > span.pb_v8 > span")
                fiyat1 = fiyat1_element.text.strip()  # Metni al ve boşlukları temizle
                fiyat1 = fiyat1.replace(" TL", "")
                fiyat1 = fiyat1.replace(".", "")
                fiyat1 = fiyat1.replace(",", ".")
                fiyat1 = float(fiyat1)
                fiyat1 = int(fiyat1)
            except ValueError as ve:
                pass
                #print(f"Değer hatası: {ve}. Fiyat değeri: {fiyat1}")
            except Exception as e:
                pass
                #print(f"Bir hata oluştu: {e}")
            try:
                fiyat2_element = driver.find_element(By.CSS_SELECTOR, f"#APL > li:nth-child({sayac}) > div > a:nth-child(2) > span.pb_v8 > span")
                fiyat2 = fiyat2_element.text.strip()  # Metni al ve boşlukları temizle
                fiyat2 = fiyat2.replace(" TL", "")
                fiyat2 = fiyat2.replace(".", "")
                fiyat2 = fiyat2.replace(",", ".") 
                fiyat2 = float(fiyat2)
                fiyat2 = int(fiyat2)
            except ValueError as ve:
                pass
                #print(f"Değer hatası: {ve}. Fiyat değeri: {fiyat2}")
            except Exception as e:
                pass
                #print(f"Bir hata oluştu: {e}")
            try:
                fiyat3_element = driver.find_element(By.CSS_SELECTOR, f"#APL > li:nth-child({sayac}) > div > a:nth-child(3) > span.pb_v8 > span")
                fiyat3 = fiyat3_element.text.strip()  # Metni al ve boşlukları temizle
                fiyat3 = fiyat3.replace(" TL", "")
                fiyat3 = fiyat3.replace(".", "")
                fiyat3 = fiyat3.replace(",", ".")
                fiyat3 = float(fiyat3)
                fiyat3 = int(fiyat3)   
            except ValueError as ve:
                pass
                #print(f"Değer hatası: {ve}. Fiyat değeri: {fiyat3}")
            except Exception as e:
                pass
                #print(f"Bir hata oluştu: {e}")
            fark = yuzdelik_fark(fiyat2,fiyat1)
            if fark >= 30:
                print(f"{fiyat1}TL {fiyat2}TL {fiyat3}TL \nArada {fark} Kadar fark var !!")
                with open("akakce.txt","a",encoding="utf-8") as akakce:
                    akakce.write(f"\n\n{urun.get_attribute("href")}\n{urun.find_element(By.TAG_NAME,'h3').text} \n {fiyat1}TL {fiyat2}TL {fiyat3}TL Arada {fark} Kadar fark var !!\n\n")
            else:
                print(f"{fiyat1}TL {fiyat2}TL {fiyat3}TL")
        except:
            sayac = 1
            try:
                nextBtn = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Sonraki')]"))
                )
            except Exception as e:
                pass
                #print("Yeni Sayfa Yuklenemedi ", e)
            time.sleep(3)
            driver.execute_script("arguments[0].click();",nextBtn)
            break
        sayac+=1
        with open("aramaSonuclari.txt","a",encoding="utf-8") as file:
            file.write(f"\n\n{urun.get_attribute("href")} \n{urun.find_element(By.TAG_NAME,'h3').text}\n{fiyat1} TL {fiyat2} TL {fiyat3} TL\n\n")
with open("aramaSonuclari.txt","a",encoding="utf-8") as file:
    file.write("Arama Bitişi.")
print(sayac)
