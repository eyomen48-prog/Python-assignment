ürünadı = input("Lütfen ürün adını giriniz: ")
ürünadeti = int(input("Lütfen ürün adedini giriniz: "))
birimfiyat = float(input("Lütfen ürünün birim fiyatını giriniz: "))
toplamfiyat = ürünadeti * birimfiyat
print(f"ürün adı: {ürünadı}")
print(f"ürün adedi: {ürünadeti}")
print(f"birim fiyat: {birimfiyat:.2f} TL")
print(f"toplam fiyat: {toplamfiyat:.2f} TL")