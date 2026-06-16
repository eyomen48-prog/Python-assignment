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