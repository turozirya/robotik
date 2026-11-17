class Battery():
    def __init__(self,capacity_mah,voltage=3.7):
        self.capacity_mah = capacity_mah
        self.voltage = voltage
        self.consumed_mah = 0  

    def drain(self,current_ma,seconds):
        self.consumed_mah += (current_ma)*(seconds/3600)
        if self.consumed_mah > self.capacity_mah:
            self.consumed_mah = self.capacity_mah
    
    def percent(self):
        return ((self.capacity_mah-self.consumed_mah)*100)/self.capacity_mah

    @classmethod
    def from_config(cls,cfg):
        try:
            capacity_mah = cfg["capacity_mah"]
        except KeyError:
            raise ValueError("capacity_mah gerekli")  # Programı durdurur ve açıklayıcı hata verir

        #voltage = cfg["voltage"] if "voltage" in cfg else 3.7 # 3,7 yazmisim tuple dondu TypeError hatasi aldim
        voltage = cfg.get("voltage", 3.7) # onceki yontem de calisti ama bu daha kisa oldu
        return cls(capacity_mah,voltage)

    @staticmethod
    def mah_to_wh(mah, volt):
        return mah * volt / 1000   # TypeError: unsupported operand type(s) for /: 'tuple' and 'int'

    def energy_wh(self):
        return self.mah_to_wh(self.capacity_mah-self.consumed_mah,self.voltage)

# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
  print("UYARI: Bu dosya bir modüldür ve tek başına çalıştırılamaz!")