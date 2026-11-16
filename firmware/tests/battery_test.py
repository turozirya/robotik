import sys
sys.path.append("lib")
from battery import *

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
    