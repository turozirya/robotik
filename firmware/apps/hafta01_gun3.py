import sys
sys.path.append("lib")
from sensor import Sensor

s1 = Sensor("sicaklik", "C", -10, 50, noise=0.5)
s2 = Sensor("mesafe", "cm", 2, 400, noise=2)

for i in range(30):
    s1.read()
    s2.read()

print("Ortalama")
print("s1:",s1.average())
print("s2:",s2.average())

print("Hata Sayisi")
print("s1:",s1.error_count)
print("s2:",s2.error_count)

print("len history")
print("s1:",len(s1.history()))
print("s2:",len(s2.history()))

print("repr")
print("s1:",s1)
print("s2:",s2)

s3 = Sensor("t", "C", 0, 100, source=lambda: 25)
s3.read()

print("Ortalama")
print("s3:",s3.average())

print("Hata Sayisi")
print("s3:",s3.error_count)

print("len history")
print("s3:",len(s3.history()))

print("repr")
print("s3:",s3)

#s4 = Sensor("x", "u", 10, 5)

h = s1.history()
h.append(9999)
print(s1.average())