import math 
yarıçap = float(input("Yarıçapı giriniz: "))
pi = math.pi
alan = pi * yarıçap ** 2
cevre = 2 * pi * yarıçap
print(f"Dairenin alanı: {alan:.2f}")
print(f"Dairenin çevresi: {cevre:.2f}")