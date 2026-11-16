# Hafta 1 — Sınıflar (16–20 Kasım 2026)

## Gün 1 — 16 Kasım

### Yaptıklarım
- Tutorial 9.1–9.3: sınıf tanımı, nesne, __init__, self, öznitelik ve metot konusunu incelendi.
- Python 3.13, VS Code ve Git kurulumu yapildi. Klasor yapisi olusturuldu. Git reposu olusturuldu. Ilk commit atildi.
- firmware/lib/ klasorune led.py, counter.py ve battery.py modul dosyalari yazildi
### Deneyler

#### Deney 1: Metottan `self` parametresini silmek
- **Ne yaptım:** apps klasorune deneme.py dosyasi olusturuldu, icine iki sinif yazildi bir metodun self parametresi silindi
- **Ne oldu:** (TypeError: Led.on() takes 0 positional arguments but 1 was given)
- **Neden:** `kirmizi.on()` yazdığında Python bunu aslında Led.on(kirmizi) olarak çalıştırır. Python nesneyi metoda ilk argüman olarak kendiliğinden gönderir; parametresi olmayan bir metot bu argümanı alamadığı için hata verir

#### Deney 2: `yesil = sari` ataması
- **Ne yaptım:** `yesil = sari` atamasi yapildi, `yesil.on()` çağrisi yapildi.
- **Ne oldu:** `yesil.on()` çağrisindan sonra sari nesneside ayni sekilde degisti
- **Neden:** `yesil = sari` ataması yapildigi icin iki isim aynı tek nesneyi gösteriyor. Eski yeşil LED nesnesine ise artık hiçbir isim ulaşamıyor.

### Hatalar

#### Hata 1: `Counter.value()` çağrılamıyor
- **Belirti:** `c.value()` çağrısı `TypeError: 'int' object is not callable` hatası verdi.
- **Neden:** `__init__` içindeki `self.value = 0` aynı adlı metodu kapattı. Python ismi önce nesnenin kendi değişkenlerinde arar.
- **Çözüm:** Sayıyı `self._value` içinde tuttum, `value()` metodu onu döndürüyor.
- **Ders:** Bir sınıfta değişken ile metoda aynı adı verme.

#### Hata 2: `Battery.drain()` harcamayı biriktirmiyor
- **Belirti:** Her`Battery.drain()` cagrisindan sonra bir onceki cagri unutuluyor. Hata vermedi ama yanlis sonuc uretti
- **Neden:** `self.consumed_mah = (current_ma)*(seconds/3600)`
- **Çözüm:** `self.consumed_mah += (current_ma)*(seconds/3600)`
- **Ders:** Kumulatif toplamlarda += kullan

#### Hata 3: Led durumlari hatali
- **Belirti:** Led durumlari yerine pin numaralari yaziyor
- **Neden:** Led sınıfının parametrelerini Led(pin, status=False) olarak değiştirdim, ama deneme kodu hâlâ eski şekilde Led('yesil', 10) diye çağırıyor.
- **Çözüm:** Cağrıları yeni parametrelere göre düzelttim, yani Led(10) gibi. __init__ içinde self.status = bool(status) degisiklikleri yapildi
- **Ders:** bir sınıfın parametrelerini değiştirdiğinde, o sınıfı kullanan bütün kodu da kontrol etmelisin

## Gün 2 — 17 Kasım
(yarın buraya)

## Haftalık değerlendirme (Cuma doldurulacak)
1. Bu hafta ne öğrendim?
2. Hangi parçayı `lib/`'e ekledim?
3. Ne ölçtüm, sonuç ne çıktı?
4. Hangi hatayla karşılaştım, nasıl çözdüm?
5. Bunu bir sonraki aşamada nerede kullanacağım?