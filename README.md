# -Python-assignments-2
1. Market Sepeti Toplamı (List) Senaryo: Bir market sepetinde ürün fiyatları var. Sepetin toplam tutarını hesapla. Veri: prices = [12.5, 45.0, 9.99, 3.75] İstenen: Toplam tutarı hesapla. Sonucu float olarak döndür. Toplamı 2 ondalık basamakla yazdır. İpucu: sum() kullanabilirsin ama önce döngüyle de deneyebilirsin.

prices = [12.5, 45.0, 9.99, 3.75]
total_price = sum(prices)
print(f"Total price of items in the cart: ${total_price:.2f}")




2.Not Ortalaması ve Geçti/Kaldı (List)
Senaryo: Bir öğrencinin sınav notları listede. Ortalama 50 ve üzeriyse geçti say.

grades = [70, 45, 90, 55, 30]
total = sum(grades)
average = total / len(grades)
print(f"Not ortalaması: {average:.2f}")
if average >= 50:
    print("Sınıf geçti.")
else:
    print("Sınıf kaldı.")





3. Rent a Car — Uygun Araçları Filtrele
(List of Dict)
Senaryo: Rent a car şirketinin araç listesi var. Kullanıcı otomatik vites ve günlük
fiyatı belli bir limitin altında olan araçları görmek istiyor.
Veri:
cars = [
{"plate": "34 ABC 01", "brand": "Renault", "model": "Clio", "auto": True, "daily": 1200},
{"plate": "34 XYZ 77", "brand": "Fiat", "model": "Egea", "auto": False, "daily": 900},
{"plate": "06 TST 06", "brand": "Toyota", "model": "Corolla", "auto": True, "daily": 1500},
]
İstenen:
auto == True ve daily <= max_price olanları filtrele.
Sonuç olarak uygun araçların plakalarını liste halinde döndür.
İpucu: List comprehension ile filtreleme çok temiz olur.


cars = []
cars.append({"plate": "34 ABC 01", "brand": "Renault", "auto": True, "daily": 1200})
cars.append({"plate": "06 XYZ 99", "brand": "Fiat", "auto": False, "daily": 800})
cars.append({"plate": "06 TST 06", "brand": "Toyota", "auto": True, "daily": 1500})
max_price = float(input("Maksimum günlük fiyatı girin: "))
for car in cars:
    if car["auto"] and car["daily"] <= max_price:
        print(f"{car['plate']} - {car['brand']} - {car['daily']} TL/gün")

plates = [car["plate"] for car in cars if car["auto"] and car["daily"] <= max_price]
print("Uygun araçların plakaları:", plates)
