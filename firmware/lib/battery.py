class Battery():
    def __init__(self,capacity_mah):
        self.capacity_mah = capacity_mah
        self.consumed_mah = 0

    def drain(self,current_ma,seconds):
        self.consumed_mah += (current_ma)*(seconds/3600)
        if self.consumed_mah > self.capacity_mah:
            self.consumed_mah = self.capacity_mah
       

    def percent(self):
        return ((self.capacity_mah-self.consumed_mah)*100)/self.capacity_mah

# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
  print("UYARI: Bu dosya bir modüldür ve tek başına çalıştırılamaz!")