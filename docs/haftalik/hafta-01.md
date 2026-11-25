# Hafta 1 — Sınıflar

## Gün 1

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

## Gün 2
### Yaptıklarım
- Tutorial 9.3.5 (sınıf ve örnek değişkenleri) ve 9.4; konusunu incelendi.
- __repr__/__str__ farkı; @classmethod ve @staticmethod konularinda okumalar yapildi.
- Led sınıfına count sınıf değişkeni eklenedi, sinif degiskeni ve nesne degiskeni olarak liste eklendi ve arasindaki fark arastirildi.
- Led sinifina __repr__ ve _str__ metodlari yazildi
- Battery sınıfına voltage parametresi,Battery.from_config(cfg) (@classmethod), Battery.mah_to_wh(mah, volt) (@staticmethod)ve energy_wh() metotlari eklendi. 
### Deneyler

#### Deney 1: Sinif ozelligini (Led.count) nesne uzerinden kullanmaya calismak (led1.count) 
- **Ne yaptım:** Sinif ozelligi olan count degiskenine nesne uzerinden atama yaptim 'kirmizi.count = 77'
- **Ne oldu:** Bu atama sınıf değişkenini değiştirmiyor, nesnenin üzerinde aynı adlı yeni bir değişken oluşturuyor.
- **Neden:** Python ismi önce nesnede, sonra sınıfta arar.

#### Deney 2: __repr__ yokken ve varken print(led) ile REPL'de yalnızca led yazmanın çıktılarını karsilastirmak.
- **Ne yaptım:** __repr__ ve __str__ metodlari yokken,sadece __repr__ varken verken print(led) ciktilari karsilastirildi
- **Ne oldu:** metotlerin ikiside yokken aldigim cikti <led.Led object at 0x7fff1277b230>, __str__ yokken __repr__ ciktisi aldim
- **Neden:** Metotlar yokken nesne adresini yazdiriyor, __repr__ varsa __str__ yoksa varsayilan olarak __repr__ yazdiriliyor

### Hatalar

#### Hata 1: print(Counter.readings) hata verdi
- **Belirti:** Consolda AttributeError: type object 'Counter' has no attribute 'readings' hatasi uretildi
- **Neden:** Nesneye ait bir ozellige sinif uzerinden ulasilmaya calisilmasi
- **Çözüm:** Nesneye ait bir ozellige nesne uzerinden ulasmak print(c1.readings)
- **Ders:** Bir ozelligin nesneye mi' sinifa mi ait oldugunu kontrol et

#### Hata 2: TypeError: unsupported operand type(s) for /: 'tuple' and 'int' hatasi
- **Belirti:** Konsolda hata mesaji cikti' program durdu
- **Neden:** Ondalik ayirici olarak ',' kullanilmasi
- **Çözüm:** Ondalik ayirici olarak '.' kullanmak
- **Ders:** Yazim yanlislarina dikkat et. Python’da virgül tuple oluşturur. Hata mesajının gösterdiği yer, hatanın kaynağı olmayabilir.

#### Hata 3: KeyError: 'capacity_mah' line 17, in from_config capacity_mah = cfg["capacity_mah"]
- **Belirti:** Konsolda hata mesaji cikti' program durdu
- **Neden:** Battery.from_config({"voltage": 7.4}) - zorunlu parametre olmadan,eksik parametre gondermek
- **Çözüm:** Battery.from_config({"capacity_mah": 2000}) - zorunlu parametreleri girmek, try/except ile ValueError hatasini yakalamak.
- **Ders:** Zorunlu parametreleri kontrol et, hata olabilecek yerlerde try/except hata kontrolu yap

#### Notun için soru: mah_to_wh metodunu @classmethod yapsaydın ne değişirdi?
- parametre olarak cls eklemem gerekirdi, def mah_to_wh(cls, mah, volt): şeklinde değiştirmek zorunda kalırdık. @classmethod zorunlu cls parametresi alir.
- Fonksiyonun içinde cls parametresini hiçbir yerde kullanmayacağımız için bu değişken hafızada ve kodda boşuna yer kaplardı. Bu metodu classmehod olarak yapsaydim sinifin ozellik ve metodlarina ulasabilirdim ama bu foksiyonda buna ihtiyacim yok.

## Gün 3
### Yaptıklarım
- Kod incelemesi yapildi
- name-Sensorun adi, unit-Olcum birimi (°C, cm, %, vb.), min_value-Kabul edilen minimum olcum, max_value-Kabul edilen maksimum olcum, noise-Olcumde olusabilecek gurultu miktari, history_size-Hafizada tutulacak maksimum olcum sayisi, source-Gercek sensor verisini saglayacak kaynak, _history-Son gecerli olcumleri saklayan liste
- read()-Yeni olcum uretmek, is_valid(value)-Olcum degerinin kabul edilen sinirlar icerisinde olup olmadigini belirlemek, average()-Gecmisteki gecerli olcumlerin aritmetik ortalamasini hesaplamak, history()-Olcumlerin gecmisini kullanıcıya sunmak, __repr__()- Sensor nesnesinin kisa metinsel halini olusturmak.
- Hangi metot neyi değiştirir? sorusunun cevabi, durumu yalnızca read() değiştirir, diğer metotlar sadece okur.

### Deneyler

#### Deney 1: Kapsülleme deneyi 
- **Ne yaptım:** history() metodunu geçici olarak kopya yerine self._history döndürecek şekilde değiştirdim. h = s1.history(), ardından h.append(9999) sensor.average() değerine baktim. 
- **Ne oldu:** Ortamaba bozuldu ortalamayi siniflarin cok disinda 493.73337830474173 olarak okudum
- **Neden:** Listeyi kopya olarak dundurmedigim icin iki isimde ayni listeyi refarans gosteriyor. Yapilan ekleme diger liste icerigini de degistiriyor.

### Hatalar

#### Hata 1: if not self.is_valid(value):UnboundLocalError: cannot access local variable 'value' where it is not associated with a value
- **Belirti:** UnboundLocalError hatasi uretildi,program durdu
- **Neden:** if self.noise > 0 value degiskeni olusturup hesaplanan deger bu degiskene ataniyor. Fakat self.noise 0 oldugunda degisken hic olusturulmuyor.
- **Çözüm:** else: value = raw_value satiri ile if durumu olusmasa bile degisken olusturuluyor
- **Ders:** If icinde degisken olustururken else durumunuda ekle

#### Hata 2: error_count degiskeni ve error_count() metodu ayni isimde 
- **Belirti:** Sayac disaridan degistirildiginda hatali sonuc uretiliyor.
- **Neden:** sayaç dışarıdan değiştirilebiliyor
- **Çözüm:** Sayıyı self._error_count içinde tut, error_count() metodu onu döndürsün.
- **Ders:** Gün 1 notuna “değişken ile metoda aynı adı verme” notu buradada gecerli. Ayni hatayi iki kere yapma . Degiskenlere ve metotlara ayni adi verme. 

## Gün 4
### Yaptıklarım
- Bağımlılık enjeksiyonu ile ilgili okumalar yapildi.
- Rasgele okunan degerler test edilemeyecegi icin sabit, bilinen degerler verildiginde sinifin davranisi onceden bilinecegi icin test sonucu gozlemlenebilir.
- sensor sinifini test etmek icin test_sensor.py dosyasi yazildi.

### Deneyler

#### Deney 1: sensor.py içinde pop(0) yerine pop()
- **Ne yaptım:** sensor.py içinde pop(0) yerine pop() yazildi
- **Ne oldu:** Degisiklikten once tum tesler gecmisti sonrasinda - test_history_respects_size_limit: gecmis yanlis: [1, 2, 3] test kaldi
- **Neden:** Liste siniri doldugunda ilk okunan degeri degil son okunan degeri sildigi icin test gecmiyor

#### Deney 2: history() metodunu kopya yerine self._history
- **Ne yaptım:** history() metodunu kopya yerine self._history döndürecek şekilde değiştirildi.
- **Ne oldu:** Degisiklikten once tum tesler gecmisti sonrasinda - - test_history_returns_copy: disaridan degisiklik ic gecmisi etkiledi test kaldi
- **Neden:** Liste kopya olarak dondurulmedigi icin gercek liste disardan degistirilebiliyor.

#### Deney 3: is_valid() içinde < işaretini <= yapma
- **Ne yaptım:** is_valid() fonksiyonu icindeki maksimum ve minimum kontrolu icin < ,<= ile degistirildi
- **Ne oldu:** Degisiklikten once tum tesler gecmisti sonrasinda - test_read_boundary_values_are_valid ve test_is_valid tesleri kaldi
- **Neden:** Aralik icinde olmasi gereken minimum deger aralik disi kaldi

### Hatalar

#### Hata 1: IndexError: list index out of range
- **Belirti:** IndexError: list index out of range hatasi uretildi,program durdu
- **Neden:** source=SequenceSource([2, 999, 4]) ile 3 elemanli liste verildiginde 4. okumada index hatasi olusuyor
- **Çözüm:** SequenceSource sinifinda donen degeri value = self._values[self._index % len(self._values)] ile ayni listeyi bastan dondurdum buda baska bir tasarim hatasina neden oldu. Hata 2 de bunu duzeltim.
- **Ders:** iter ile nesne olusturuken dongu sonunu kontrol ettir.

#### Hata 2: SequenceSource tasarim hatasi
- **Belirti:** SequenceSource liste sinira ulastiginda tekrar bastan deger uretiyor
- **Neden:** value = self._values[self._index % len(self._values)] ile liste sonunda mod aldigim icin tekrar ilk degeri gonduruyor.
- **Çözüm:** SequenceSource sinifinda degil kullanilan yerde try except ile hata yakalayarak problem cozuldu.
- **Ders:** hata cikabilecek yerlerde hatayi try except ile yakala

#### Soru 1 : assert_raises_value_error(func, *args, **kwargs) fonksiyonu Sensor sınıfının parametrelerini nasıl iletiyor?
- Python'da fonksiyon marapetre sayisi sabit degilse disaridan tuple(demet) yada dictionary(sozluk)seklinde paremetre verebiliyoruz.
- Fonksiyonlar *args ile tuple, **kwargs ile dictionary seklinde parametre alabiliyor

#### Soru 2 : SequenceSource() parametresiz oluşturulduğunda neden 1, 2, 3… döndürüyor?
- Bunu sinirsiz sayina nesne olusturabilmek icin yaptim. SequenceSource ile sadece liste dondurdugumuzde liste eleman sayisi kadar okuma yapabiliyorduk. istedigimiz kadar okuma yapabilmek icin parametresiz cagrildiginda index arttirilip deger olarak donduruluyor.

## Haftalık değerlendirme (Cuma doldurulacak)
1. Bu hafta ne öğrendim?
2. Hangi parçayı `lib/`'e ekledim?
3. Ne ölçtüm, sonuç ne çıktı?
4. Hangi hatayla karşılaştım, nasıl çözdüm?
5. Bunu bir sonraki aşamada nerede kullanacağım?