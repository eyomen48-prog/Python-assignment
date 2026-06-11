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




4. Telefon Rehberi — Numara Bul (Dict)
Senaryo: Basit bir telefon rehberi sözlüğü var. Kullanıcı isim girince numarasını
bulmak istiyor.
Veri:
phonebook = {"Ayşe": "0532...", "Mehmet": "0505...", "Zeynep": "0544..."}
İstenen:
name verildiğinde numarayı döndür.
Kişi yoksa “Kayıt bulunamadı” döndür.
İpucu: dict.get(name, "Kayıt bulunamadı") en basit yol.


phonebook = {"Ayşe": "1234567890", "Mehmet": "0587654321", "Zeynep": "5555555555"}
name = input("isim giriniz: ")
if name in phonebook:
    print(f"{name} numarası: {phonebook[name]}")
else:    print(f"{name} rehberde bulunamadı.")




5. Günlük Harcama Takibi — Toplam ve En
Yüksek (List)
Senaryo: Bir hafta boyunca günlük harcamaların listede.
Veri:
expenses = [120, 0, 75, 200, 50, 30, 90]
İstenen:
Toplam harcamayı bul.
En yüksek harcama yapılan günü (index + 1 şeklinde gün numarası) bul. Harcama 0 olan günleri ayrıca listele.
İpucu: En yüksek için max() ve index için list.index() kullanılabilir.



expenses = [120, 0, 75, 200, 50, 30, 90]
total_expenses = sum(expenses)
average_expense = total_expenses / len(expenses)
print(f"Toplam Harcama: {total_expenses} TL")
en_yüksek_harcama = max(expenses)
en_düşük_harcama = min(expenses)
gun = expenses.index(en_yüksek_harcama)  +1
print(f"En Yüksek Harcama: {gun}. günde: {en_yüksek_harcama}  TL")
for i in range(len(expenses)): 
    if expenses [i] == 0:
        print(f"{i+1}. günde harcama yapılmadı.")



        6. Kargo Takip — Durum Güncelle (Dict)
Senaryo: Bir kargo takip sistemi var. tracking sözlüğünde takip no → durum
tutuluyor.
Veri:
tracking = {"TR123": "Yolda", "TR124": "Şubede", "TR125": "Teslim edildi"}
İstenen:
update_status(tracking, code, new_status) fonksiyonu yaz.
Kod yoksa yeni kayıt eklesin.
Eski durum ve yeni durumu yazdır (log gibi).
İpucu: tracking[code] = new_status her iki durumda da iş görür; ama önce eskiyi get
ile al.



tracking = {"TR123": "Yolda", "TR124": "Şubede", "TR125": "Teslim Edildi"}

def update_status(tracking_code, new_status):
    eski_durum = tracking.get(tracking_code, "Yeni kayıt")
    tracking[tracking_code] = new_status
    print(f"{tracking_code}: {eski_durum} → {new_status}")

update_status("TR123", "Teslim Edildi")
update_status("TR999", "Yolda")



7. Alışveriş Listesi — Yinelenenleri
Temizle (List)
Senaryo: Kullanıcı aynı ürünü birden fazla kez yazmış.
Veri:
items = ["süt", "ekmek", "süt", "peynir", "ekmek", "yoğurt"]
İstenen:
Sıralamayı bozmadan tekrarları kaldır.
Çıktı: ["süt", "ekmek", "peynir", "yoğurt"]
İpucu: Bir seen listesi veya dict ile kontrol edebilirsin. (Set kullanmak kolay ama
sırayı bozabilir.)


items = ["süt" , "ekmek" , "süt" , "peynir" , "ekmek" , "yoğurt"]
seen = []
for item in items:
    if item not in seen:
      
        seen.append(item)
print(seen)



8. Restoran Menü — KDV Dahil Fiyat (Dict)
Senaryo: Menüde ürün adı → fiyat var. KDV %10 eklenecek.
Veri:
menu = {"Hamburger": 180, "Pizza": 220, "Ayran": 30}
İstenen:
Her ürünün KDV dahil fiyatını hesapla.
Yeni bir dict döndür: {"Hamburger": 198.0, ...}
İpucu: dict comprehension: {k: v*1.10 for k, v in menu.items()}


menu = {"Hamburger": 180, "Pizza": 220, "Ayran":30}

kdvli_menu = {}
for item, price in menu.items():
    kdvli_menu[item] = price * 1.10
print("KDV'li Menü:", kdvli_menu)
