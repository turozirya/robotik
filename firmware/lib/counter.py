class Counter():
    
    def __init__(self,step=1):
        self._value = 0
        self.step = step 
        self.readings = []      

    def increment(self):
        self._value += self.step

    def reset(self):
        self._value = 0

    def value(self):
        return self._value

    def add_list(self,x):
        self.readings.append(x)

# Dosya doğrudan çalıştırıldığında burası devreye girer
if __name__ == "__main__":
  print("UYARI: Bu dosya bir modüldür ve tek başına çalıştırılamaz!")