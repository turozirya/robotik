class Led():
    def __init__(self,isim,pin,durum=0):
        self.isim = isim
        self.pin = pin
        self.durum = durum

    def on(self):
        self.durum = 1
        print(f'{self.isim} Led Acildi')

    def off(self):
        self.durum = 0
        print(f'{self.isim} Led Kapatildi')

    def toggle(self):
        self.durum = 1 if self.durum == 0 else 0
        print(f'{self.isim} Led in Durumu Degisti')

    def is_on(self):
        return self.durum

# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
  print("UYARI: Bu dosya bir modüldür ve tek başına çalıştırılamaz!")