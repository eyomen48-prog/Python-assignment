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
