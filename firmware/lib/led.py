class Led():
    def __init__(self,pin,status=False):  
        self.pin = pin
        self.status= status

    def on(self):
        self.status = True

    def off(self):
        self.status = False
        
    def toggle(self):
        self.status = not self.status        

    def is_on(self):
        return self.status

# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
  print("UYARI: Bu dosya bir modüldür ve tek başına çalıştırılamaz!")