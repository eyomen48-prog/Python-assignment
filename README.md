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


9. Öğrenci Not Defteri — Ders Bazlı
Ortalama (Dict of List)
Senaryo: Her dersin içinde not listesi var.
Veri:
grades_by_course = {
"Matematik": [70, 85, 90],
"Türkçe": [60, 75],
"Fizik": [40, 55, 65]
}
İstenen:
Her ders için ortalama notu hesapla.
Sonuç dict olsun: {"Matematik": 81.67, ...} (2 ondalık)
İpucu: Döngü içinde sum(list)/len(list).

grades_by_course = {
    "Matematik": [70, 85, 90],
    "Türkçe": [80, 88, 92],
    "Fizik": [75, 82, 88]
}
averages = {}

# 1. döngü: ortalamaları hesapla
for ders, notlar in grades_by_course.items():
    averages[ders] = sum(notlar) / len(notlar)

# 2. döngü: yazdır
for ders, ort in averages.items():
    print(f"{ders}: {ort:.2f}")


2. Rent a Car — Kiralama Gün Sayısı ve
Toplam Ücret (Dict)
Senaryo: Bir araç kiralandı. Günlük fiyat ve kiralama başlangıç/bitiş gün sayısı
veriliyor.
Veri Örneği:
rental = {"plate": "34 ABC 01", "daily": 1200, "days": 3}
İstenen:
Toplam ücreti hesapla: daily * days
Eğer days <= 0 ise hata mesajı döndür.
İpucu: Validasyon (doğrulama) her zaman ilk adım.




rental = {"plate": "34 ABC 01", "daily": 1200, "days":3}

if rental["days"] <= 0:
    print("Hata!")
else:
    total = rental["daily"] * rental["days"]
    print(f"Total rental cost for {rental['plate']} is: {total} TL")





    11) E-Ticaret Sepeti — Ürün Adedi Say
(List)
Senaryo: Kullanıcının sepetinde ürün ID’leri listeleniyor. Aynı ürün birden fazla
kez olabilir.
Veri:
cart = ["SKU1", "SKU2", "SKU1", "SKU3", "SKU2", "SKU1"]
İstenen:
Her SKU’nun adedini sayan bir dict üret.
Çıktı örneği: {"SKU1": 3, "SKU2": 2, "SKU3": 1}
İpucu: “frequency map” mantığı: counts[sku] = counts.get(sku, 0) +
   


cart = ["SKU1", "SKU2", "SKU1", "SKU3", "SKU2", "SKU1"]

counts = {}  # boş dict

for sku in cart:
    counts[sku] = counts.get(sku, 0) + 1

print(counts)




12. Hastane Randevu — Doktora Göre
Listele (List of Dict)
Senaryo: Randevular listesinde doktor adı ve saat var. Doktor bazlı grupla.
Veri:
appointments = [
{"doctor": "Dr. Can", "time": "09:00", "patient": "Ali"},
{"doctor": "Dr. Can", "time": "10:30", "patient": "Ayşe"},
{"doctor": "Dr. Ece", "time": "09:15", "patient": "Mehmet"},
]
İstenen:
Çıktı dict: doktor → randevu listesi
Örn: {"Dr. Can": [{"time":..., "patient":...}, ...], "Dr. Ece": [...]}
Doktor yoksa otomatik liste oluştur.
İpucu: setdefault veya if doctor not in grouped: ile liste başlat.

appointments = [
    {"doctor": "Dr. Can", "time": "09:00", "patient": "Ali"},
    {"doctor": "Dr. Can", "time": "10:30", "patient": "Ayşe"},
    {"doctor": "Dr. Ece", "time": "09:15", "patient": "Mehmet"},
]
grouped = {}
for appointment in appointments:
    grouped.setdefault(appointment["doctor"], []).append(appointment)
print(grouped)





13. Film Listesi — En Yüksek Puanlı İlk 3
(List of Dict)
Senaryo: Filmler puanlarıyla listeleniyor.
Veri:
movies = [
{"title": "Film A", "rating": 7.2},
{"title": "Film B", "rating": 8.9},
{"title": "Film C", "rating": 8.1},
{"title": "Film D", "rating": 9.0},
]
İstenen:
Puanı en yüksekten düşüğe sırala.
İlk 3 filmin adlarını listele.
İpucu: sorted(movies, key=lambda x: x["rating"], reverse=True).



movies = [
{"title": "Film A", "rating": 7.2},
{"title": "Film B", "rating": 8.9},
{"title": "Film C", "rating": 8.1},
{"title": "Film D", "rating": 9.0},

]
print(sorted(movies, key=lambda x: x["rating"], reverse=True)[:3])
for film in sorted(movies, key=lambda x: x["rating"], reverse=True)[:3]:
    print(film["title"])




   14. Kasa İşlemleri — Gün Sonu Bakiye
(List)
Senaryo: Gün içinde kasa hareketleri listesi var. Pozitif: para girişi, negatif: para
çıkışı.
Veri:
transactions = [1000, -200, -150, 500, -50]
İstenen:
Gün sonu bakiyeyi hesapla.
En büyük gideri (en küçük negatif değeri) bul.
Sadece giderleri ayrı listede döndür.
İpucu: Giderleri filtrelemek için t < 0 koşulu.


transactions = [1000, -200, -150, 500, -50]
total = 0
for transaction in transactions:
    total += transaction
print("Toplam Kasa İşlemi:", total)

total_sum = sum(transactions)
print("Toplam Kasa İşlemi (sum ile):", total_sum)
giderler = [transaction for transaction in transactions if transaction < 0]
print("Giderler:", giderler)
gelirler = [transaction for transaction in transactions if transaction > 0]
print("Gelirler:", gelirler)

toplam_gider = sum(giderler)
print("Toplam Gider:", toplam_gider)

toplam_gelir = sum(gelirler)
print("Toplam Gelir:", toplam_gelir)
net_kasa = toplam_gelir - toplam_gider
print("Net Kasa Durumu:", net_kasa)
en_büyük_gider = min(giderler)
print("En Büyük Gider:", en_büyük_gider)
en_büyük_gelir = max(gelirler)
print("En Büyük Gelir:", en_büyük_gelir)



15. Log Analizi — Hata Mesajlarını Say (List
of Dict)
Senaryo: Uygulama log’larında seviye ve mesaj var.
Veri:
logs = [
{"level": "INFO", "msg": "Started"},
{"level": "ERROR", "msg": "DB connection failed"},
{"level": "ERROR", "msg": "DB connection failed"},
{"level": "WARN", "msg": "Retrying"},
]
İstenen:
Sadece ERROR seviyesindeki mesajları say.
Çıktı dict: mesaj → kaç kez
İpucu: Önce filtrele, sonra frequency map.

logs = [
    {"level": "INFO", "msg": "Started"},
    {"level": "ERROR", "msg": "DB connection failed"},
    {"level": "ERROR", "msg": "DB connection failed"},
    {"level": "WARN",  "msg": "Retrying"},
]
log = {"level": "ERROR", "msg": "DB connection failed"}
errors = [log for log in logs if log["level"] == "ERROR"]
print(errors)
frequency = {} 
for log in errors:
    mesaj = log["msg"]


    if mesaj in frequency:
        frequency[mesaj] = frequency[mesaj] + 1
    else:
        frequency[mesaj] = 1

print(frequency)





16. Kütüphane — Ödünç Alınan Kitaplar
(Dict of Dict)
Senaryo: Kullanıcı → ödünç aldığı kitaplar listesi tutuluyor. Yeni ödünç
verilecek.
Veri:
borrows = {
"Ali": {"books": ["1984", "Dune"]},
"Ayşe": {"books": ["Sefiller"]}
}
İstenen:
borrow_book(borrows, user, book) fonksiyonu yaz.
Kullanıcı yoksa oluştur.
Aynı kitabı tekrar ekleme (zaten varsa değişiklik yapma).
İpucu: “var mı” kontrolü: if book not in borrows[user]["books"]:.

borrows = {
    "Ali": {"books": ["1984", "Dune"]},
    "Ayşe": {"books": ["Sefiller"]}
}
def borrow_book(borrows, user, book):
    if user not in borrows:          
        borrows[user] = {"books": []}
    
    if book not in borrows[user]["books"]:   
        borrows[user]["books"].append(book)

borrow_book(borrows, "Ali", "Şeker Portakalı") 
borrow_book(borrows, "Mehmet", "Dune")  
print(borrows)




17. Sınav Sonuçları — En Başarılı Öğrenci
(List of Dict)
Senaryo: Öğrencilerin adı ve puanı var.
Veri:
students = [
{"name": "Ali", "score": 78},
{"name": "Ayşe", "score": 92},
{"name": "Mehmet", "score": 88},
]
İstenen:
En yüksek puanlı öğrenciyi bul. Hem adı hem puanı döndür.
Puanlar eşitse alfabetik olarak adı önce geleni seç.
İpucu: sorted(..., key=...) ile önce puan sonra isim sırası kurabilirsin.

students = [
    {"name": "Ali", "score": 78},
    {"name": "Ayşe", "score": 92},
    {"name": "Mehmet", "score": 88},

]
sirali = sorted(students, key=lambda s: (-s["score"], s["name"]))
print(sirali[0])



18. Stok Yönetimi — Kritik Stok Listesi
(Dict)
(Dict)
Senaryo: Ürün → stok adedi var. Kritik stok eşiği 5.
Veri:
stock = {"SKU1": 10,
"SKU2": 3,
"SKU3": 0,
İstenen:
Stoku 5’in altında olanları filtrele.
Çıktı: {"SKU2": 3,
"SKU3": 0}
"SKU4": 7}
İpucu: dict comprehension ile filtreleme.


stock = {
    "SKU1": 10,
    "SKU2": 3,
    "SKU3": 0,
    "SKU4": 7
}
kritik_stok = {key: value for key, value in stock.items() if value < 5}

print(kritik_stok)




19.  Rent a Car — Kirada Olan Araçları Ayır
(List of Dict)
(List of Dict)
Senaryo: Araç listesinde status alanı var:
“
available
”
,
“
rented”
,
“
maintenance
”
.
İstenen:
Kirada olanları ayrı listeye koy.
Müsait olanların sayısını bul.
Bakımdaki araçların plakalarını listeler.
İpucu: Birden fazla filtreyi ayrı ayrı yazmak okunabilirliği artırır



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



20. spor Takımı — Oyuncu İstatistikleri
Toplama (Dict)
Toplama (Dict)
Senaryo: Oyuncu adı → maç başına gol listesi var. Sezon toplam golü hesapla.
Veri:
goals = {
"Ahmet": [1, 0, 2, 1],
"Burak": [0, 0, 1],
"Can": [2, 2, 0, 1, 0],
}
İstenen:
Her oyuncu için toplam gol: dict
En çok gol atan oyuncu: adı + toplam
İpucu: sum(list) ile hızlı, ama boş liste olabilir mi? Kural koy.




goals = {
    "Ahmet": [1, 0, 2, 1],
    "Burak": [0, 0, 1],
    "Can": [2, 2, 0, 1, 0],
}
print(goals)
toplam_goller = {oyuncu: sum(gol_listesi) for oyuncu, gol_listesi in goals.items()}
print(toplam_goller)
en_iyi_oyuncu = max(toplam_goller, key=toplam_goller.get)
print(en_iyi_oyuncu)
print(en_iyi_oyuncu, toplam_goller[en_iyi_oyuncu])




21. Yemek Tarifi — Malzeme Birleştirme
(List)
(List)
Senaryo: İki farklı alışveriş listesi var (ev ve misafir). Tek liste yapıp tekrarları
temizle.
Veri:
home = ["un"
,
"şeker"
,
"yumurta"]
guest = ["şeker"
,
"süt"
,
"çikolata"]
İstenen:
Listeyi birleştir, tekrarları sıralamayı bozmadan sil.
İpucu: Önce home + guest, sonra 7. sorudaki mantık.


home = ["un", "şeker", "yumurta"]
guest = ["şeker", "süt", "çikolata"]

birlesik = home + guest

sonuc = []
for eleman in birlesik:
    if eleman not in sonuc:
        sonuc.append(eleman)

print(sonuc)





22. Online Kurs — Öğrenci Katılım Raporu
(List of Dict)
(List of Dict)
Senaryo: Her kayıt bir öğrencinin bir derse katılımını temsil ediyor.
Veri:
attendance = [
{"student": "Ali"
,
{"student": "Ali"
,
{"student": "Ayşe"
,
{"student": "Ali"
,
]
"lesson": "Python"
,
"minutes": 45},
"lesson": "SQL"
,
"minutes": 30},
"lesson": "Python"
,
"minutes": 60},
"lesson": "Python"
,
"minutes": 15},
İstenen:
Öğrenci bazında toplam dakika: dict
Ayrıca ders bazında toplam dakika: dict
İpucu: Aynı veri üzerinden iki ayrı
“toplama sözlüğü” tut.


attendance = [
    {"student": "Ali", "lesson": "Python", "minutes": 45},
    {"student": "Ali", "lesson": "SQL", "minutes": 30},
    {"student": "Ayşe", "lesson": "Python", "minutes": 60},
    {"student": "Ali", "lesson": "Python", "minutes": 15},
]
print(attendance)
öğrenci_toplam = {}
ders_toplam = {}
for kayit in attendance:
    isim = kayit["student"]
    ders = kayit["lesson"]
    dakika = kayit["minutes"]
    öğrenci_toplam[isim] = öğrenci_toplam.get(isim, 0) + dakika
    ders_toplam[ders] = ders_toplam.get(ders, 0) + dakika
print(ders_toplam)
print(öğrenci_toplam)



23. Siparişler — Şehre Göre Ciro (List of
Dict)Dict)
Senaryo: Siparişlerin şehir ve tutarı var. Şehir bazında ciroyu topla.
Veri:
orders = [
{"city": "İstanbul"
,
{"city": "Ankara"
,
{"city": "İstanbul"
,
]
"total": 1200},
"total": 800},
"total": 500},
İstenen:
Şehir → toplam ciro dict’i döndür.
En yüksek ciroyu getiren şehri bul.
İpucu: city_
totals[city] = city_
totals.get(city, 0) + total


orders = [
    {"city": "İstanbul", "total": 1200},
    {"city": "Ankara", "total": 800},
    {"city": "İstanbul", "total": 500},
]
city_totals = {}
for order in orders:
    city = order["city"]
    total = order["total"]

    city_totals[city] = city_totals.get(city, 0) + total

print(city_totals)
en_yuksek_sehir = max(city_totals, key=city_totals.get)
print(en_yuksek_sehir)
print(en_yuksek_sehir, city_totals[en_yuksek_sehir])




24. Anket Sonuçları — Seçenek Frekansı ve
Yüzde (List)
Yüzde (List)
Senaryo: Kullanıcılar bir ankette seçenek işaretliyor.
Veri:
answers = ["A"
,
İstenen:
"B"
,
"A"
,
"C"
,
"A"
,
"B"]
Frekans dict’i çıkar.
Her seçeneğin yüzde oranını hesapla (toplam üzerinden).
Sonucu örn: {"A": {"count": 3,
"pct": 50.0}, ...}
İpucu: Önce say, sonra yüzdeyi hesaplamak daha kolay.

answers = ["A", "B", "A", "C", "A", "B"]

frekans = {}
for cevap in answers:
    if cevap in frekans:
        frekans[cevap] = frekans[cevap] + 1
    else:
        frekans[cevap] = 1

toplam = len(answers)

sonuc = {}
for secenek, sayi in frekans.items():
   sonuc[secenek] = {"count": sayi, "pct": round((sayi / toplam) * 100, 2)}

print(sonuc)



25. Metin Analizi — Kelime Sayacı (List &
Dict)
Dict)
Senaryo: Bir metindeki kelimelerin kaç kez geçtiğini say.
Veri:
text =
İstenen:
"Bugün hava çok güzel bugün dışarı çıkmak güzel"
Metni küçük harfe çevir.
Kelimelere ayır.
Frekans sözlüğü döndür.
En sık geçen ilk 3 kelimeyi bul.
İpucu: split() başlangıç için yeter; noktalama yok sayılabilir (şimdilik).


text = "Bugün hava çok güzel bugün dışarı çıkmak güzel"
kelimeler = text.lower().split()
print(kelimeler)
frekans = {}
for kelime in kelimeler:
    if kelime in frekans:
        frekans[kelime] = frekans[kelime] + 1
    else:
        frekans[kelime] = 1

print(frekans)

sirali = sorted(frekans.items(), key=lambda x: x[1], reverse=True)
print(sirali)
print(sirali[:3])





26. Banka — Hesap Hareketleri ve Kategori
Bazlı Özet (List of Dict)
Bazlı Özet (List of Dict)
Senaryo: Banka harcama kayıtlarında kategori ve tutar var (negatif: gider,
pozitif: gelir).
Veri:
bank = [
{"category": "Maaş"
,
{"category": "Market"
,
{"category": "Ulaşım"
,
{"category": "Market"
,
]
"amount": 30000},
"amount": -850},
"amount": -120},
"amount": -230},
İstenen:
Kategori bazında toplamları topla.
Sadece gider kategorilerini ayrı raporla.
Toplam net bakiyeyi hesapla.
İpucu: Gider mi gelir mi? amount < 0 kontrolü.



bank = [
    {"category": "Maaş",    "amount": 30000},
    {"category": "Market",  "amount": -850},
    {"category": "Ulaşım",  "amount": -120},
    {"category": "Market",  "amount": -230},
]
kategori_toplam = {}
for hareket in bank:
    kategori = hareket["category"]
    tutar = hareket["amount"]
    if kategori in kategori_toplam:
        kategori_toplam[kategori] = kategori_toplam[kategori] + tutar
    else:
        kategori_toplam[kategori] = tutar

print(kategori_toplam)
giderler = {}
for kategori, toplam in kategori_toplam.items():
    if toplam < 0:
        giderler[kategori] = toplam

print(giderler)
net_bakiye = sum(hareket["amount"] for hareket in bank)
print(net_bakiye)




27. Rent a Car — Müşteri Kiralama
Geçmişi (Nested Dict)
Geçmişi (Nested Dict)
Senaryo: Müşteri → kiralamalar listesi (her kiralama bir dict). Yeni kiralama
ekleniyor, aynı gün aynı plakaya izin yok.
İstenen:
add
_
rental(history, customer, rental) fonksiyonu yaz.
rental örn: {"date": "2026-02-18"
,
"plate": "
"
...
,
"days": 2}
Aynı müşteri aynı tarihte aynı plakayı tekrar kiralayamaz (ekleme yapma,uyarı döndür).
İpucu: Eklemeden önce liste içinde dolaşıp
“
aynı date ve plate var mı
” kontrol



def add_rental(history, customer, rental):

    if customer not in history:
        history[customer] = []

    for existing_rental in history[customer]:
        if existing_rental["date"] == rental["date"] and existing_rental["plate"] == rental["plate"]:
            return f"UYARI: {customer} adlı müşteri {rental['date']} tarihinde {rental['plate']} plakalı aracı zaten kiralamış!"
    

    history[customer].append(rental)
    return f"Kiralama başarıyla eklendi: {customer} → {rental['plate']} ({rental['date']})"




history = {}
print(add_rental(history, "Ahmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 2}))
print(add_rental(history, "Ahmet", {"date": "2026-02-20", "plate": "34ABC123", "days": 1}))
print(add_rental(history, "Ahmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 3})) 
print(add_rental(history, "Mehmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 2}))
print("\nGüncel history:")
for customer, rentals in history.items():
    print(f"  {customer}: {rentals}")




28. Depo — Raf Barkod Doğrulama (List &
Dict)
Dict)
Senaryo: Depoda raf barkodları belirli formatta: warehouseIdXshelfIdXcolumnXrow.
Örn:
"12X3X2X5"
.
İstenen:
Bir barkod verildiğinde parçala (split).
Her parçanın sayısal olup olmadığını kontrol et.
Depo ID’
si verilen depo listesinde var mı kontrol et.
İpucu: parts = barcode.split("X") ve str.isdigit() kullan.


def validate_barcode(barcode, warehouses):
    parts = barcode.split("X")
    all_digits = all(part.isdigit() for part in parts)
    
    if not all_digits:
        return "HATA: Barkod sadece sayısal değerler içermeli!"
    
    warehouse_id = int(parts[0])
    if warehouse_id not in warehouses:
        return "HATA: Depo bulunamadı!"
    
    return "Depo bulundu!"

warehouses = [12, 45, 7]
print(validate_barcode("12X3X2X5", warehouses))
print(validate_barcode("99X3X2X5", warehouses))
print(validate_barcode("12X3XaX5", warehouses))
