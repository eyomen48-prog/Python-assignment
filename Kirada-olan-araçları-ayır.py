cars = [
    {"plaka": "34ABC123", "status": "available"},
    {"plaka": "34DEF456", "status": "rented"},
    {"plaka": "34GHI789", "status": "maintenance"},
    {"plaka": "34JKL012", "status": "rented"},
]
kirada = [car for car in cars if car["status"] == "rented"]
print(kirada)
musait = [car for car in cars if car["status"] == "available"]
musait_sayisi = len(musait)
print(musait_sayisi)
bakimda = [car for car in cars if car["status"] == "maintenance"]
plakalar = [car["plaka"] for car in bakimda]
print(plakalar)
