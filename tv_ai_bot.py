#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
  📺 ANDROID TV SEÇMELİ MEDYA VE REKLAM ENGELLEME BOTU
====================================================================
  Geliştirici : Mesut Salih Öztürk
  E-Posta     : msozturk86@gmail.com
  Instagram   : @yoldakiseruven
  Telif Hakkı : © 2026 Mesut Salih Öztürk
  Lisans      : MIT License (Açık Kaynak)
====================================================================
  AÇIKLAMA:
  Google Play, ayarlar ve temel sistem servislerine dokunmaz.
  Reklam servisleri ve Netflix/Amazon gibi medya uygulamalarını 
  tek tek ekrana getirerek sizden Evet/Hayır onayı alır.
====================================================================
"""

import subprocess
import sys
import socket
import concurrent.futures
from datetime import datetime

# --- TEK TEK SORULACAK REKLAM VE MEDYA UYGULAMALARI ---
DENETLENECEK_LISTE = [
    ("com.google.android.tvrecommendations", "Ana Ekran Reklam ve Öneri Servisi"),
    ("com.google.android.onboarding.tv", "Kurulum ve Reklam İzleme Servisi"),
    ("com.netflix.ninja", "Netflix Uygulaması"),
    ("com.amazon.amazonvideo.livingroom", "Amazon Prime Video Uygulaması"),
    ("com.google.android.play.games", "Google Play Oyunlar")
]

TIMEOUT_SURESI = 10 

def otomatik_tv_bul(port=5555, zaman_asimi=0.5):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        kendi_ip = s.getsockname()[0]
    except Exception:
        return []
    finally:
        s.close()
    
    ip_blogu = kendi_ip.rsplit('.', 1)[0] + '.'
    hedef_ipler = [f"{ip_blogu}{i}" for i in range(1, 255)]
    bulunan_cihazlar = []
    
    def port_kontrol(ip):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(zaman_asimi)
                s.connect((ip, port))
            return ip
        except:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        sonuclar = executor.map(port_kontrol, hedef_ipler)
        for sonuc in sonuclar:
            if sonuc:
                bulunan_cihazlar.append(sonuc)
    return bulunan_cihazlar

print("\n==================================================")
print("    📺 TV SEÇMELİ MEDYA & REKLAM ENGELLEME BOTU")
print("==================================================")
print(" 👨‍💻 Geliştirici : Mesut Salih Öztürk")
print(" ✉️  E-Posta     : msozturk86@gmail.com")
print(" 📸 Instagram   : @yoldakiseruven")
print("==================================================\n")

print("Yerel ağınızdaki televizyonlar taranıyor (5-10 saniye sürer)...")
tv_cihazlari = otomatik_tv_bul()

if not tv_cihazlari:
    print("Ağda otomatik port açığı olan bir Android TV bulunamadı.")
    tv_ip = input("Lütfen TV IP adresini manuel girin (Çıkış için 'q'): ").strip()
    if tv_ip.lower() == 'q':
        sys.exit(0)
elif len(tv_cihazlari) == 1:
    tv_ip = tv_cihazlari[0]
    print(f"[BAŞARILI] Televizyon otomatik tespit edildi: {tv_ip}")
else:
    print("\nAğda birden fazla cihaz algılandı:")
    for i, ip in enumerate(tv_cihazlari, 1):
        print(f"{i}. Cihaz IP: {ip}")
    secim = input("Bağlanmak istediğiniz cihazın numarasını girin: ")
    try:
        tv_ip = tv_cihazlari[int(secim)-1]
    except:
        print("Hatalı seçim! İşlem iptal edildi.")
        sys.exit(1)

print(f"\n{tv_ip} adresine ADB üzerinden bağlanılıyor...")

try:
    subprocess.run(["adb", "connect", tv_ip], check=True, timeout=TIMEOUT_SURESI, stdout=subprocess.DEVNULL)
    cihazlar = subprocess.run(["adb", "devices"], capture_output=True, text=True).stdout
    if tv_ip not in cihazlar:
        print("HATA: Bağlantı reddedildi. TV ekranından USB/Ağ hata ayıklama iznini onaylayın.")
        sys.exit(1)
except Exception as e:
    print(f"HATA: Bağlantı kurulamadı. Detay: {e}")
    sys.exit(1)

# --- RAM & ÖNBELLEK / ZRAM HIZLANDIRMA ---
print("\n--- PERFORMANS OPTİMİZASYONU ---")
zram_onay = input("[?] Kanal geçişlerini ve arayüzü hızlandırmak için önbellek temizliği yapılsın mı? (e/h): ").strip().lower()
if zram_onay == 'e':
    try:
        subprocess.run(["adb", "shell", "echo 3 > /proc/sys/vm/drop_caches"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[OK] Sistem önbelleği boşaltıldı, RAM ferahlatıldı.")
    except Exception as e:
        print(f"UYARI: Önbellek temizlenemedi ({e}).")

# --- TEK TEK ONAYLI DONDURMA İŞLEMİ ---
print("\n--- UYGULAMA VE REKLAM DENETİMİ BAŞLATILIYOR ---")
print("Google Play, Ayarlar ve Remap tamamen koruma altındadır.")
basarili_islemler = []

for pkg, aciklama in DENETLENECEK_LISTE:
    while True:
        tek_onay = input(f"\n[?] Dondurulsun mü? -> {aciklama}\n    ({pkg})\n(e: Evet / h: Hayır / q: İşlemi Bitir): ").strip().lower()
        
        if tek_onay == 'q':
            print("İşlem kullanıcı tarafından sonlandırıldı.")
            break
        elif tek_onay == 'e':
            try:
                subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", pkg], 
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=TIMEOUT_SURESI)
                print(f"[OK] Donduruldu: {aciklama}")
                basarili_islemler.append(pkg)
            except subprocess.TimeoutExpired:
                print(f"UYARI: {pkg} atlandı (Zaman aşımı).")
            break
        elif tek_onay == 'h':
            print(f"[PAS GEÇİLDİ] Dokunulmadı: {aciklama}")
            break
        else:
            print("Hatalı tuşlama! Lütfen sadece 'e', 'h' veya 'q' tuşlayın.")
            
    if tek_onay == 'q':
        break

# İşlem kayıtlarının loglanması
if basarili_islemler:
    zaman = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("tv_islem_log.txt", "a", encoding="utf-8") as log_dosyasi:
        log_dosyasi.write(f"\n--- İŞLEM TARİHİ: {zaman} | CİHAZ IP: {tv_ip} ---\n")
        for b_pkg in basarili_islemler:
            log_dosyasi.write(f"- {b_pkg}\n")
    print(f"\n[BİLGİ] İşlemler 'tv_islem_log.txt' dosyasına kaydedildi.")

print("\nOptimizasyon süreci başarıyla tamamlandı!")
subprocess.run(["adb", "disconnect", tv_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
