import sys
sys.path.append("lib")
from led import Led
from counter import Counter
from battery import Battery
from dene import Dene


# 1
kirmizi = Led(1)
kirmizi.count = 77 # count kirmizi nesnesine ait bir degisken oldu
sari = Led(2)
yesil = Led(3)
mor = Led(4)

print(Led.count)
print(sari.count)
print(kirmizi.count)

# 2.1  Sinifa ait liste 

c1 = Dene(1)
c2 = Dene(2)

c1.add_list('kirmizi led')
c2.add_list('yesil led')

#print(Counter.readings) # cikti: ['kirmizi led', 'yesil led']
#print(c1.readings) # cikti: ['kirmizi led', 'yesil led']
#print(c2.readings) # cikti: ['kirmizi led', 'yesil led']


# 2.2 Nesneye ait liste

c1 = Dene(1)
c2 = Dene(2)

c1.add_list('kirmizi led')
c2.add_list('yesil led')

#print(Counter.readings) # HATA: AttributeError: type object 'Counter' has no attribute 'readings'
print(c1.readings) # cikti: ['kirmizi led']
print(c2.readings) # cikti: ['yesil led']

# 3
print(repr(kirmizi))
kirmizi.on()
print(repr(kirmizi))

print(kirmizi)
print(yesil)

# 4

pil = Battery.from_config({"capacity_mah": 2000, "voltage": 7.4})

#print(pil.capacity_mah) # 2000 
#print(pil.voltage) # (7.4, 7) tuple dondu

print(pil.energy_wh())

pil.drain(1000, 3600)
print(pil.energy_wh())

pil2 = Battery.from_config({"capacity_mah": 1000})

print(pil2.energy_wh())

print(Battery.mah_to_wh(1000, 3.7))

#Battery.from_config({"voltage": 7.4})  # ValueError: capacity_mah gerekli
