import sys
sys.path.append("lib")
from led import Led
from counter import Counter
from battery import Battery

# 3 Led Deneme
print('---------------3 Led Deneme---------------')

yesil = Led(10)
sari = Led(11)
kirmizi = Led(12)

print('ilk durum')
print(f'yesil: {yesil.is_on()}',end='\t')
print(f'sari: {sari.is_on()}',end='\t\t')
print(f'kirmizi: {kirmizi.is_on()}')


print('ikinci durum')
sari.on()
kirmizi.toggle()

print(f'yesil: {yesil.is_on()}',end='\t')
print(f'sari: {sari.is_on()}',end='\t\t')
print(f'kirmizi: {kirmizi.is_on()}')


print('ucuncu durum')
yesil.toggle()
sari.off()

print(f'yesil: {yesil.is_on()}',end='\t')
print(f'sari: {sari.is_on()}',end='\t\t')
print(f'kirmizi: {kirmizi.is_on()}')

print('dorduncu durum yesil = sari')

yesil = sari

yesil.on()

print(f'sari: {sari.is_on()}')

yesil.off()

print(f'sari: {sari.is_on()}')



# Sayac Deneme
print('---------------Sayac Deneme---------------')

sayac1 = Counter(step=1) # 1 er 1 er artar
sayac2 = Counter(10)     # 10 ar 10 ar artar

print('ilk degerler')
print('sayac1: ',sayac1.value())
print('sayac2: ',sayac2.value())

sayac1.increment()
sayac1.increment()
sayac2.increment()

print('son degerler')
print('sayac1: ',sayac1.value())
print('sayac2: ',sayac2.value())

sayac1.reset()
sayac2.reset()

print('resetlenen degerler')
print('sayac1: ',sayac1.value())
print('sayac2: ',sayac2.value())

# Battery Deneme
print('---------------Battery Deneme---------------')

lipo1 = Battery(1000)

print('pil durumu %',lipo1.percent())

lipo1.drain(500,1800)

print('pil durumu %',lipo1.percent())

lipo1.drain(500,1800)

print('pil durumu %',lipo1.percent())

lipo1.drain(500,1800)

print('pil durumu %',lipo1.percent())

lipo1.drain(500,1800)

print('pil durumu %',lipo1.percent())

lipo1.drain(500,1800)

print('pil durumu %',lipo1.percent())