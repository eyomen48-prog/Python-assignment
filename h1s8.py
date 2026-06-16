indirim = float(input("İndirim oranını giriniz: "))
fiyat = float(input("Ürünün fiyatını giriniz: "))
indirim_miktari = fiyat * indirim / 100
indirimli_fiyat = fiyat - indirim_miktari
print(f"Orijinal fiyat: {fiyat:.2f}")
print(f"İndirim oranı: {indirim:.2f}%")
print(f"İndirim miktarı: {indirim_miktari:.2f}")
print(f"İndirimli fiyat: {indirimli_fiyat:.2f}")


