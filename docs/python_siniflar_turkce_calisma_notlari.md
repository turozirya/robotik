# Python'da Sınıflar ve Nesne Yönelimli Programlama

**Türkçe çalışma notu --- Python Tutorial, "Classes" bölümündeki konu
başlıkları temel alınarak özgün anlatımla hazırlanmıştır.**

Kaynak: [Python Resmî Dokümantasyonu ---
Classes](https://docs.python.org/3/tutorial/classes.html)

> Bu doküman birebir çeviri değildir. Konuları Türkçe açıklamalar, yeni
> örnekler ve uygulama notlarıyla öğretici bir biçimde ele alır. Kodlar
> Python 3 içindir.

## İçindekiler

1.  Nesneler, isimler ve referanslar
2.  İsim alanları ve kapsamlar
3.  Sınıflara giriş
4.  Sınıf ve örnek nesneleri
5.  `self`, kurucu metot ve metot çağrısı
6.  Sınıf değişkenleri ve örnek değişkenleri
7.  Özellik arama ve sınıflarla ilgili notlar
8.  Kalıtım
9.  Çoklu kalıtım ve MRO
10. Kapsülleme yaklaşımı ve özel isimler
11. Dataclasses
12. Yineleyiciler (iterators)
13. Üreteçler (generators)
14. Üreteç ifadeleri
15. Otonom robotik için bütünleştirici örnek
16. Alıştırmalar ve cevap anahtarı

------------------------------------------------------------------------

## 1. Nesneler, isimler ve referanslar

Python'da sayılar, metinler, listeler, fonksiyonlar ve sınıflar dâhil
her değer bir nesnedir. Bir değişken, nesnenin kendisini içine koyan bir
kutu gibi düşünülmemelidir; nesneye verilen bir isim veya referans gibi
düşünülmelidir.

``` python
sicaklik = 24
oda_sicakligi = sicaklik

print(sicaklik)       # 24
print(oda_sicakligi)  # 24
```

Değişken isimleri aynı nesneyi gösterebilir. Bu duruma **takma ad
(aliasing)** denir. Özellikle listeler gibi değiştirilebilir nesnelerde
önemlidir:

``` python
ilk_liste = [10, 20, 30]
ikinci_isim = ilk_liste

ikinci_isim.append(40)

print(ilk_liste)  # [10, 20, 30, 40]
```

İki isim de aynı liste nesnesini gösterdiği için yapılan değişiklik her
iki isimden erişildiğinde görülür.

Bağımsız bir kopya gerekiyorsa:

``` python
ilk_liste = [10, 20, 30]
kopya = ilk_liste.copy()

kopya.append(40)

print(ilk_liste)  # [10, 20, 30]
print(kopya)      # [10, 20, 30, 40]
```

**Önemli:** `int`, `float`, `str` ve `tuple` gibi temel türler
değiştirilemez (immutable); `list`, `dict` ve `set` ise değiştirilebilir
(mutable) türlerdir.

## 2. İsim alanları ve kapsamlar

### 2.1. İsim alanı (namespace)

İsim alanı, isimleri nesnelere bağlayan bir eşlemedir. Örneğin bir
modülün değişkenleri, bir fonksiyonun yerel değişkenleri ve bir nesnenin
özellikleri farklı isim alanlarında bulunabilir.

Aynı isim farklı isim alanlarında çakışmadan kullanılabilir:

``` python
hiz = 10

def motoru_hazirla():
    hiz = 5
    print("Fonksiyon içindeki hız:", hiz)

motoru_hazirla()
print("Modüldeki hız:", hiz)
```

Çıktı:

``` text
Fonksiyon içindeki hız: 5
Modüldeki hız: 10
```

### 2.2. Kapsam (scope)

Kapsam, bir isme doğrudan erişilebilen kod bölgesidir. Python isim
ararken genel olarak şu sırayı izler:

1.  **Local:** Geçerli fonksiyonun yerel alanı
2.  **Enclosing:** İç içe fonksiyonlarda dış fonksiyonların alanı
3.  **Global:** Modül düzeyindeki alan
4.  **Built-in:** Python'ın yerleşik isimleri

Bu arama sırası LEGB olarak bilinir.

### 2.3. `global` ve `nonlocal`

`global`, modül düzeyindeki bir isme atama yapmak istediğimizi belirtir:

``` python
sayac = 0

def sayaci_artir():
    global sayac
    sayac += 1

sayaci_artir()
print(sayac)  # 1
```

`nonlocal`, iç içe fonksiyonlarda en yakın dış fonksiyonun değişkenine
atama yapar:

``` python
def sayac_olustur():
    sayi = 0

    def artir():
        nonlocal sayi
        sayi += 1
        return sayi

    return artir

sayac = sayac_olustur()
print(sayac())  # 1
print(sayac())  # 2
```

**Pratik not:** `global` kullanımını gereksiz yere artırmak kodun
takibini zorlaştırabilir. Durum bilgisini çoğu zaman sınıf örneğinde
tutmak daha düzenlidir.

## 3. Sınıflara giriş

Sınıf (class), benzer özellik ve davranışlara sahip nesneler oluşturmak
için kullanılan bir şablondur.

-   **Özellik (attribute):** Nesnenin tuttuğu veri.
-   **Metot (method):** Sınıf içinde tanımlanan ve nesne üzerinden
    çağrılan fonksiyon.
-   **Örnek (instance):** Bir sınıftan oluşturulmuş somut nesne.

Örneğin bir robotun sınıfı; adı, pil seviyesi ve hareket etme
davranışını tanımlayabilir. Farklı robot nesneleri bu sınıftan
üretilebilir.

``` python
class Robot:
    def selam_ver(self):
        print("Merhaba, ben bir robotum!")

robot1 = Robot()
robot1.selam_ver()
```

Sınıf adlarında yaygın Python yazım geleneği **PascalCase**
kullanmaktır: `Robot`, `MesafeSensoru`, `MotorSurucusu`.

Sınıf tanımı çalıştırıldığında Python bir sınıf nesnesi oluşturur. Sınıf
adını fonksiyon çağırır gibi kullanmak yeni bir örnek üretir.

## 4. Sınıf ve örnek nesneleri

Sınıfın kendisine ait özellikler ile o sınıftan oluşturulan örneklerin
özellikleri birbirinden ayrılmalıdır.

``` python
class Sensor:
    tur = "mesafe"

sensor1 = Sensor()
sensor2 = Sensor()

print(sensor1.tur)  # mesafe
print(sensor2.tur)  # mesafe
```

`Sensor.tur` sınıf niteliğidir. Örneğe özel bir değer atandığında örnek
niteliği oluşur:

``` python
sensor1.tur = "sicaklik"

print(sensor1.tur)  # sicaklik
print(sensor2.tur)  # mesafe
print(Sensor.tur)   # mesafe
```

Bir örneğin özelliklerine nokta ile erişilir: `sensor1.tur`.

## 5. `self`, kurucu metot ve metot çağrısı

### 5.1. `__init__()` metodu

`__init__`, yeni örnek oluşturulduktan sonra başlangıç değerlerini
ayarlamak için otomatik çağrılan özel metottur. Günlük kullanımda kurucu
metot olarak anılır.

``` python
class Robot:
    def __init__(self, isim, pil):
        self.isim = isim
        self.pil = pil

robot = Robot("Gezgin", 100)

print(robot.isim)  # Gezgin
print(robot.pil)   # 100
```

`self`, metot çağrısının yapıldığı örneği gösterir. Python'da özel bir
anahtar kelime değildir; ilk parametre için yerleşmiş bir adlandırma
geleneğidir. Bu geleneğe uymak kodu diğer Python programcıları için daha
anlaşılır kılar.

### 5.2. Örnek metotları

``` python
class Robot:
    def __init__(self, isim, pil):
        self.isim = isim
        self.pil = pil

    def bilgi_goster(self):
        print(f"{self.isim}: pil seviyesi %{self.pil}")

    def pil_tuket(self, miktar):
        self.pil -= miktar

robot = Robot("Gezgin", 100)
robot.bilgi_goster()
robot.pil_tuket(15)
robot.bilgi_goster()
```

`robot.bilgi_goster()` çağrısında `robot` örneği `self` parametresine
otomatik aktarılır. Bu çağrı kavramsal olarak
`Robot.bilgi_goster(robot)` biçimindedir.

### 5.3. Metotların birbirini çağırması

``` python
class Robot:
    def __init__(self):
        self.pil = 100

    def pil_tuket(self, miktar):
        self.pil -= miktar

    def kisa_gorev(self):
        self.pil_tuket(5)
        self.pil_tuket(5)

robot = Robot()
robot.kisa_gorev()
print(robot.pil)  # 90
```

Bir metodun içinden aynı nesnenin başka bir metoduna `self.metot_adi()`
şeklinde erişilir.

## 6. Sınıf değişkenleri ve örnek değişkenleri

**Sınıf değişkeni**, tüm örnekler tarafından ortak kullanılan bilgidir.
**Örnek değişkeni** ise her nesneye ait ayrı bilgidir.

``` python
class Robot:
    platform = "UNIHIKER"

    def __init__(self, isim):
        self.isim = isim

robot_a = Robot("Gezgin")
robot_b = Robot("Kesifci")

print(robot_a.platform)  # UNIHIKER
print(robot_b.platform)  # UNIHIKER
print(robot_a.isim)      # Gezgin
print(robot_b.isim)      # Kesifci
```

### 6.1. Değiştirilebilir sınıf değişkenlerine dikkat

Liste veya sözlük gibi değiştirilebilir bir nesneyi sınıf değişkeni
yapmak, bütün örneklerin aynı koleksiyonu paylaşmasına yol açabilir:

``` python
class Robot:
    gorevler = []  # Dikkat: bütün örnekler paylaşır

    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)

a = Robot()
b = Robot()

a.gorev_ekle("Harita olustur")
b.gorev_ekle("Engelden kacin")

print(a.gorevler)
# ['Harita olustur', 'Engelden kacin']
```

Her robotun ayrı görev listesi olması isteniyorsa liste `__init__`
içinde oluşturulmalıdır:

``` python
class Robot:
    def __init__(self):
        self.gorevler = []

    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)

a = Robot()
b = Robot()

a.gorev_ekle("Harita olustur")
b.gorev_ekle("Engelden kacin")

print(a.gorevler)  # ['Harita olustur']
print(b.gorevler)  # ['Engelden kacin']
```

**Kural:** Örneğe özel listeleri ve sözlükleri çoğunlukla `__init__`
içinde `self` üzerinden oluşturun.

## 7. Özellik arama ve sınıflarla ilgili notlar

Python bir özellik istendiğinde önce örneğin kendi özelliklerine, sonra
sınıfına ve gerektiğinde üst sınıflarına bakar. Bu nedenle örneğe ait
bir değer, aynı isimli sınıf değerini gölgeler.

``` python
class Arac:
    enerji_turu = "elektrik"

arac1 = Arac()
arac2 = Arac()

arac2.enerji_turu = "hibrit"

print(arac1.enerji_turu)  # elektrik
print(arac2.enerji_turu)  # hibrit
print(Arac.enerji_turu)    # elektrik
```

Python'da nesne verilerini diğer kodlardan tamamen gizleyen katı bir
`private` mekanizması yoktur. Bu nedenle sınıfın sunduğu metotları
kullanmak ve özellikleri gelişigüzel değiştirmemek iyi bir tasarım
yaklaşımıdır.

Bir nesnenin türü `type()` ile görülebilir:

``` python
deger = Robot()
print(type(deger))
```

## 8. Kalıtım (inheritance)

Kalıtım, yeni bir sınıfın başka bir sınıfın özellik ve metotlarından
yararlanmasını sağlar.

-   **Üst sınıf (base/parent class):** Ortak davranışları tanımlar.
-   **Alt sınıf (derived/child class):** Üst sınıftan miras alır ve yeni
    davranış ekleyebilir.

``` python
class Robot:
    def __init__(self, isim):
        self.isim = isim

    def baslat(self):
        print(f"{self.isim} baslatildi.")

class MobilRobot(Robot):
    def hareket_et(self):
        print(f"{self.isim} hareket ediyor.")

gezgin = MobilRobot("Gezgin")
gezgin.baslat()
gezgin.hareket_et()
```

`MobilRobot`, `Robot` sınıfının `__init__` ve `baslat` özelliklerinden
yararlanır.

### 8.1. Metot ezme (override)

Alt sınıf, üst sınıftaki bir metodu kendi ihtiyacına göre yeniden
tanımlayabilir:

``` python
class Robot:
    def durum(self):
        print("Robot hazir.")

class MobilRobot(Robot):
    def durum(self):
        print("Mobil robot hareket etmeye hazir.")

robot = MobilRobot()
robot.durum()
```

### 8.2. `super()`

Üst sınıfın davranışını genişletmek için `super()` kullanılır:

``` python
class Robot:
    def __init__(self, isim):
        self.isim = isim

class SensorluRobot(Robot):
    def __init__(self, isim, sensor_sayisi):
        super().__init__(isim)
        self.sensor_sayisi = sensor_sayisi

robot = SensorluRobot("Kesifci", 3)
print(robot.isim)
print(robot.sensor_sayisi)
```

`super().__init__(isim)`, üst sınıfın başlangıç işlemlerini çalıştırır.

### 8.3. Tür kontrolü

``` python
print(isinstance(robot, SensorluRobot))  # True
print(isinstance(robot, Robot))          # True
print(issubclass(SensorluRobot, Robot))  # True
```

-   `isinstance(nesne, Sinif)`: Nesnenin belirtilen sınıfın örneği olup
    olmadığını kontrol eder.
-   `issubclass(Alt, Ust)`: Bir sınıfın diğerinden türeyip türemediğini
    kontrol eder.

## 9. Çoklu kalıtım ve MRO

Bir sınıf birden fazla sınıftan kalıtım alabilir:

``` python
class Kamera:
    def fotograf_cek(self):
        print("Fotograf cekildi.")

class MesafeOlcer:
    def mesafe_olc(self):
        print("Mesafe olculdu.")

class AkilliRobot(Kamera, MesafeOlcer):
    pass

robot = AkilliRobot()
robot.fotograf_cek()
robot.mesafe_olc()
```

Bir metot birden fazla üst sınıfta bulunuyorsa Python hangi sırayla
arama yapacağını **Method Resolution Order (MRO)** ile belirler.

``` python
print(AkilliRobot.mro())
```

Çoklu kalıtımda `super()` ve MRO birlikte çalışır. Karmaşık sınıf
hiyerarşilerinde metotların hangi sırayla çağrıldığını `mro()` ile
incelemek yararlıdır. Çoklu kalıtımı yalnızca tasarıma gerçek bir katkı
sağlıyorsa tercih edin.

## 10. Kapsülleme yaklaşımı ve özel isimler

Python'da alt çizgi kullanımı erişim niyetini ifade eden bir gelenektir:

-   `acik_isim`: Normal, herkese açık isim.
-   `_dahili_deger`: Dahili kullanım için olduğu belirtilen isim.
-   `__sinif_ozel`: İsim çakışmalarını azaltmak için isim dönüştürme
    (name mangling) uygulanır.

``` python
class Pil:
    def __init__(self, seviye):
        self._seviye = seviye

    def seviye_goster(self):
        return self._seviye

pil = Pil(80)
print(pil.seviye_goster())
```

Tek alt çizgi, "Bu alan sınıfın iç uygulamasına aittir; doğrudan
kullanımı tercih etmeyin" mesajı verir. Bu, teknik olarak erişimi
engellemez.

Çift alt çizgi ise isim dönüştürme uygular:

``` python
class Ornek:
    def __init__(self):
        self.__deger = 42

nesne = Ornek()
print(nesne._Ornek__deger)  # Teknik olarak erişilebilir; normal kullanım önerilmez.
```

Çift alt çizgiyi gerçek bir güvenlik veya gizlilik sınırı olarak
görmeyin. Temel amacı alt sınıflardaki isim çakışmalarını azaltmaktır.

## 11. Dataclasses

Sınıfın temel amacı bir grup veriyi bir arada tutmaksa `dataclasses`
modülü gereksiz tekrarları azaltabilir.

``` python
from dataclasses import dataclass

@dataclass
class SensorVerisi:
    sicaklik: float
    nem: float
    mesafe: int

veri = SensorVerisi(24.5, 45.0, 120)

print(veri)
print(veri.sicaklik)
```

`@dataclass`, alanlara göre `__init__` ve okunabilir bir metin gösterimi
gibi yaygın metotları otomatik oluşturur.

Veri sınıfları; sensör ölçümlerini, robot konumunu veya görev
parametrelerini taşımak için kullanışlıdır.

## 12. Yineleyiciler (iterators)

Bir yineleyici, elemanları tek tek sağlayan nesnedir. Listeler,
demetler, metinler ve sözlükler üzerinde `for` döngüsü kurabilmemizin
arkasında yineleme protokolü vardır.

-   `iter(nesne)`: Yineleyiciyi elde eder.
-   `next(yineleyici)`: Sıradaki elemanı verir.
-   Eleman kalmadığında `StopIteration` oluşur; `for` döngüsü bunu
    otomatik olarak yönetir.

``` python
renkler = ["kirmizi", "yesil", "mavi"]
it = iter(renkler)

print(next(it))  # kirmizi
print(next(it))  # yesil
print(next(it))  # mavi
```

### 12.1. Kendi yineleyicimizi yazmak

Bir sınıf `__iter__()` ve `__next__()` metotlarını tanımlayarak
yinelenebilir davranış sağlayabilir:

``` python
class GeriSayim:
    def __init__(self, baslangic):
        self.sayi = baslangic

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi < 1:
            raise StopIteration

        sonuc = self.sayi
        self.sayi -= 1
        return sonuc

for sayi in GeriSayim(3):
    print(sayi)
```

Çıktı:

``` text
3
2
1
```

Bu örnekte nesne hem yinelenebilir hem de yineleyicidir. Aynı nesne
ikinci kez dolaşıldığında sayaç bitmiş olacağından yeni bir geri sayım
başlamaz.

## 13. Üreteçler (generators)

Üreteçler, yineleyici oluşturmanın daha kısa bir yoludur. Normal bir
fonksiyona benzerler; ancak `return` yerine değer üretmek için `yield`
kullanırlar.

``` python
def geri_sayim(baslangic):
    while baslangic > 0:
        yield baslangic
        baslangic -= 1

for sayi in geri_sayim(3):
    print(sayi)
```

`yield` çalıştığında fonksiyon duraklar. Bir sonraki değer istendiğinde
kaldığı yerden devam eder. Böylece tüm sonuçları baştan bir listeye
doldurmak gerekmez.

Sensör verilerini sırayla işlemek için de üreteç kullanılabilir:

``` python
def sensor_olcumleri():
    olcumler = [21.5, 21.7, 22.0, 22.2]

    for deger in olcumler:
        yield deger

for sicaklik in sensor_olcumleri():
    print("Sicaklik:", sicaklik)
```

Gerçek zamanlı sistemlerde veriyi parça parça işlemek bellek kullanımını
azaltmaya yardımcı olabilir.

## 14. Üreteç ifadeleri (generator expressions)

Liste üreteçlerine benzeyen, ancak köşeli parantez yerine normal
parantez kullanan kısa ifadelerdir.

``` python
kareler = (sayi * sayi for sayi in range(5))

for kare in kareler:
    print(kare)
```

Liste üreteci ile farkı:

``` python
liste = [sayi * sayi for sayi in range(5)]
uretec = (sayi * sayi for sayi in range(5))
```

-   Liste üreteci sonuçların tamamını bellekte tutar.
-   Üreteç ifadesi değerleri ihtiyaç oldukça üretir.

Toplam gibi işlemlerde kullanışlıdır:

``` python
toplam = sum(sayi * sayi for sayi in range(10))
print(toplam)  # 285
```

## 15. Otonom robotik için bütünleştirici örnek

Aşağıdaki örnek, sınıf, örnek değişkeni, metot, kalıtım ve dataclass
kavramlarını küçük bir robot modeli üzerinde bir araya getirir. Donanımı
kontrol etmez; programlama kavramlarını simüle eder.

``` python
from dataclasses import dataclass

@dataclass
class MesafeOlcumu:
    santimetre: float

class Robot:
    def __init__(self, isim):
        self.isim = isim
        self.pil = 100

    def durum_goster(self):
        print(f"{self.isim} | Pil: %{self.pil}")

class OtonomRobot(Robot):
    GUVENLI_MESAFE = 20

    def karar_ver(self, olcum):
        if olcum.santimetre < self.GUVENLI_MESAFE:
            return "DUR"
        return "ILERLE"

    def gorevi_isle(self, olcum):
        karar = self.karar_ver(olcum)
        print(f"Olculen mesafe: {olcum.santimetre} cm")
        print(f"Karar: {karar}")
        self.pil -= 1

robot = OtonomRobot("Gezgin")

olcumler = [
    MesafeOlcumu(50),
    MesafeOlcumu(35),
    MesafeOlcumu(12),
]

for olcum in olcumler:
    robot.gorevi_isle(olcum)

robot.durum_goster()
```

Bu örnekte:

-   `Robot` ortak robot özelliklerini tanımlar.
-   `OtonomRobot`, `Robot` sınıfından kalıtım alır.
-   `MesafeOlcumu`, sensör verisini düzenli biçimde taşır.
-   `karar_ver()` ölçüme göre basit bir karar üretir.
-   `GUVENLI_MESAFE` sınıf değişkenidir.
-   `pil` her robot örneğine ait bir örnek değişkenidir.

Gerçek bir robotta sensör sürücüsü, motor kontrolü, hata yönetimi ve
güvenli durdurma mekanizmaları ayrıca tasarlanmalıdır.

## 16. Alıştırmalar

### Alıştırma 1 --- Sınıf oluşturma

`Motor` adında bir sınıf yazın. `hiz` ve `aktif` özellikleri olsun.
`baslat()` metodu motoru aktif hâle getirsin.

### Alıştırma 2 --- Sınıf ve örnek değişkeni

`Robot` sınıfında `platform = "UNIHIKER"` sınıf değişkenini tanımlayın.
İki robot oluşturun ve her birine farklı isim verin.

### Alıştırma 3 --- Kalıtım

`Sensor` sınıfından `SicaklikSensoru` sınıfını türetin. Alt sınıfa
`birim = "C"` özelliğini ekleyin.

### Alıştırma 4 --- Dataclass

`Konum` adında bir veri sınıfı yazın. `x`, `y` ve `yon` alanlarını
içersin.

### Alıştırma 5 --- Üreteç

1'den başlayarak verilen sayıya kadar çift sayıları üreten bir
`cift_sayilar()` üreteci yazın.

### Alıştırma 6 --- Robot kararı

Bir `OtonomRobot` sınıfı yazın. `mesafe` 20 cm'den küçükse `"DUR"`,
değilse `"ILERLE"` döndüren bir metot ekleyin.

## 17. Alıştırmalar için örnek cevaplar

``` python
# 1. Motor
class Motor:
    def __init__(self):
        self.hiz = 0
        self.aktif = False

    def baslat(self):
        self.aktif = True


# 2. Sınıf ve örnek değişkeni
class Robot:
    platform = "UNIHIKER"

    def __init__(self, isim):
        self.isim = isim


# 3. Kalıtım
class Sensor:
    pass

class SicaklikSensoru(Sensor):
    birim = "C"


# 4. Dataclass
from dataclasses import dataclass

@dataclass
class Konum:
    x: float
    y: float
    yon: float


# 5. Üreteç
def cift_sayilar(sinir):
    for sayi in range(2, sinir + 1, 2):
        yield sayi


# 6. Basit karar sınıfı
class OtonomRobot:
    def karar_ver(self, mesafe):
        if mesafe < 20:
            return "DUR"
        return "ILERLE"
```

------------------------------------------------------------------------

## Hızlı tekrar

  Kavram              Kısa açıklama
  ------------------- ---------------------------------------------
  Class               Nesnelerin şablonu
  Instance            Sınıftan oluşturulan nesne
  Attribute           Nesnenin veya sınıfın niteliği
  Method              Sınıf içinde tanımlanan fonksiyon
  `self`              Metodun üzerinde çalıştığı örnek
  `__init__`          Örnek başlangıç değerlerini ayarlar
  Class variable      Örnekler arasında paylaşılan sınıf niteliği
  Instance variable   Her örneğe ait nitelik
  Inheritance         Bir sınıfın başka sınıftan özellik alması
  Override            Üst sınıf metodunu yeniden tanımlama
  `super()`           Üst sınıf davranışına erişme
  Iterator            Değerleri sırayla sağlayan nesne
  Generator           `yield` ile değer üreten fonksiyon
  Dataclass           Veri taşıyan sınıfları kolaylaştıran araç

## Önerilen çalışma sırası

1.  Önce 1--7. bölümleri çalışın; sınıf ve nesne mantığını
    sağlamlaştırın.
2.  8--10. bölümlerde kalıtım ve sınıf tasarımını öğrenin.
3.  11--14. bölümlerde veri taşıma ve verimli veri işleme konularını
    çalışın.
4.  15. bölümdeki robot örneğini kendiniz yeniden yazın.
5.  Alıştırmaları cevaplara bakmadan çözün.

**Resmî başvuru:** [Python Tutorial ---
Classes](https://docs.python.org/3/tutorial/classes.html)
