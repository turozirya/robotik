import sys
sys.path.append("lib")
from led import *

yesil = Led('yesil',10)
sari = Led('sari',11)
kirmizi = Led('kirmizi',12)

print('---------------ilk durum---------------')
print(f'{yesil.isim}: {yesil.is_on()}',end='\t')
print(f'{sari.isim}: {sari.is_on()}',end='\t\t')
print(f'{kirmizi.isim}: {kirmizi.is_on()}')


print('---------------ikinci durum---------------')
sari.on()
kirmizi.toggle()

print(f'{yesil.isim}: {yesil.is_on()}',end='\t')
print(f'{sari.isim}: {sari.is_on()}',end='\t\t')
print(f'{kirmizi.isim}: {kirmizi.is_on()}')


print('---------------ucuncu durum---------------')
yesil.toggle()
sari.off()

print(f'{yesil.isim}: {yesil.is_on()}',end='\t')
print(f'{sari.isim}: {sari.is_on()}',end='\t\t')
print(f'{kirmizi.isim}: {kirmizi.is_on()}')


print('---------------dorduncu durum---------------')

yesil = sari

print(f'{yesil.isim}: {yesil.is_on()}',end='\t')
print(f'{sari.isim}: {sari.is_on()}',end='\t\t')
print(f'{kirmizi.isim}: {kirmizi.is_on()}')


