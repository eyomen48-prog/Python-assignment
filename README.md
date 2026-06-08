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
