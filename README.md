# #!/usr/bin/env python3
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
  ⚠️ SORUMLULUK REDDİ (DISCLAIMER):
  Bu scriptin kullanımıyla ilgili tüm sorumluluk tamamen kullanıcıya 
  aittir. Yanlış paket dondurma veya sistem müdahalelerinden doğabilecek 
  sorunlardan geliştirici sorumlu tutulamaz.
====================================================================
"""

📺 Android TV Hibrit &amp; Seçmeli Optimizasyon Botu
Termux'u Güncelleme ve Gerekli Araçları Kurma

​Termux paket yöneticisini güncelleyin ve Python ile Git araçlarını telefonunuza veya tabletinize yükleyin.
​Termux ekranına sırasıyla bu komutları yazıp Enter tuşuna basın:

pkg update && pkg upgrade -y

Ardından Git, Python ve ADB araçlarını kurun:
pkg install git python android-tools -y

Termux'ta ana dizininizdeyken şu komutu yazın: git clone https://github.com/yoldakiseruven/ai-tv-optimizer.git
İndirilen projelerin bulunduğu klasörün içine girmek için cd komutunu kullanın: cd ai-tv-optimizer

Android TV ve Termux Bağlantısını Hazırlama

​Botu çalıştırmadan önce televizyonunuzda şu hazırlıkların tam olduğundan emin olun:
​Aynı Wi-Fi Ağı: Telefonunuz (Termux) ve Android TV'niz kesinlikle aynı kablosuz ağa (Wi-Fi) bağlı olmalıdır.
​Ağ Hata Ayıklama (ADB Debugging): TV'nizin Ayarlar -> Cihaz Tercihleri -> Hakkında bölümüne gidip Derleme (Build) yazısının üzerine kumanda ile 7-8 kez üst üste basarak Geliştirici Seçenekleri'ni açın. Ardından Geliştirici Seçenekleri içerisinden Ağ Hata Ayıklama (Network Debugging) özelliğini Açık konuma getirin.
Botu Çalıştırma ve Kullanma
​python tv_ai_bot.py
Uygulamanın Çalışma Akışı:
​Bot yerel ağınızı tarar ve televizyonunuzun IP adresini otomatik olarak tespit edip bağlanır.
​İlk bağlantıda TV ekranında "Ağ hata ayıklama iznine izin verilsin mi?" uyarısı çıkarsa kumandanızdan "İzin Ver" seçeneğini onaylayın.
​Bot önce ZRAM / önbellek temizliği yaparak kanal geçişlerini ve arayüzü hızlandırmak isteyip istemediğinizi sorar (e / h).
​Ardından reklam servislerini, Netflix ve Amazon gibi medya uygulamalarını sırayla tek tek ekrana getirerek:
​[?] Dondurulsun mü? -> Netflix Uygulaması
(e: Evet / h: Hayır / q: İşlemi Bitir):
​şeklinde size tek tek soracaktır. İstediklerinize e diyerek dondurabilir, istemediklerinize h diyerek geçebilirsiniz.
​Bu adımları izleyerek projeyi her zaman GitHub'dan güncel haliyle çekebilir ve televizyonunuzu sorunsuz bir şekilde optimize edebilirsiniz!
içindeyken botu başlatmak için şu komutu girin
