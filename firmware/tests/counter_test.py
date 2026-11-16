import sys
sys.path.append("lib")
from counter import *

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