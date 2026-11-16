import sys
sys.path.append("lib")
from led import *
from counter import *
from battery import *

# 3 Led Deneme

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




# Sayac Deneme

sayac1 = Counter(step=1) # 1 er 1 er artar
sayac2 = Counter(10)     # 10 ar 10 ar artar

print('---------------ilk degerler---------------')
print('sayac1: ',sayac1.value)
print('sayac2: ',sayac2.value)

sayac1.increment()
sayac1.increment()
sayac2.increment()

print('---------------son degerler---------------')
print('sayac1: ',sayac1.value)
print('sayac2: ',sayac2.value)

sayac1.reset()
sayac2.reset()

print('---------------resetlenen degerler---------------')
print('sayac1: ',sayac1.value)
print('sayac2: ',sayac2.value)

# Battery Deneme

lipo1 = Battery(500)

print('pil durumu %',lipo1.percent())

current = 1000

for t in range(0,3600,100):
    print('Harcaniyor...')
    lipo1.drain(current,t)
    print('pil durumu %',lipo1.percent())
    if lipo1.percent()<30:
        print('UYARI Pil dusuk')                        # pil %30 altindaysa cik
        break
    