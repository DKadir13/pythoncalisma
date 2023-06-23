import tkinter as tk  # tkinter modülünü içe aktar

from selenium import webdriver  # Selenium'ı içe aktar
from selenium.webdriver.common.by import By  # By modülünü içe aktar

import time  # time modülünü içe aktar

def get_followers():
    username = entry.get()  # Kullanıcı adını entry widget'ından al

    driver = webdriver.Chrome()  # WebDriver'ı başlat (Chrome kullanılıyor)
    driver.get(f"https://www.instagram.com/{username}")  # Kullanıcının profil sayfasına git

    time.sleep(10)  # 3 saniye bekle

    follower_count = driver.find_element(By.XPATH, "//a[@href='/{username}/followers/']/span")  # Takipçi sayısını bul
    followers = follower_count.get_attribute("title")  # Takipçi sayısını al

    driver.quit()  # WebDriver'ı kapat

    result_label.config(text=f"Takipçi Sayısı: {followers}")  # Sonuç etiketinin metin özelliğini güncelle

# Tkinter arayüzünü oluştur
window = tk.Tk()  # Tkinter penceresi oluştur
window.title("Instagram Takipçi Sayısı")  # Pencere başlığını ayarla
window.geometry("300x150")  # Pencere boyutunu ayarla

label = tk.Label(window, text="Kullanıcı Adı:")  # Etiket oluştur
label.pack()  # Etiketi pencereye ekle

entry = tk.Entry(window)  # Giriş kutusu oluştur
entry.pack()  # Giriş kutusunu pencereye ekle

button = tk.Button(window, text="Takipçi Sayısını Getir", command=get_followers)  # Buton oluştur
button.pack()  # Butonu pencereye ekle

result_label = tk.Label(window, text="")  # Sonuç etiketi oluştur
result_label.pack()  # Sonuç etiketini pencereye ekle

window.mainloop()  # Pencereyi çalıştır
