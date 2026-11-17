class Led():
    count = 0       # sinif degiskeni
    def __init__(self,pin,status=False):  
        self.pin = pin
        self.status= bool(status)
        Led.count+=1  # her nesne olusurken sinif degiskeni 1 artar

    def on(self):
        self.status = True

    def off(self):
        self.status = False
        
    def toggle(self):
        self.status = not self.status        

    def is_on(self):
        return self.status

    def __str__(self):
        return f"LED {self.pin}: {'AÇIK' if self.status else 'KAPALI'}"

    def __repr__(self):
        return f"Led(pin={self.pin},status={self.status})"

# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
  print("UYARI: Bu dosya bir modüldür ve tek başına çalıştırılamaz!")