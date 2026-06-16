cüzdandakipara = float(input("Cüzdandaki para miktarını girin: "))
alışveriş = float(input("Alışveriş tutarını girin: "))
kalanpara = cüzdandakipara - alışveriş
if kalanpara < 0:
    print("Yetersiz bakiye!")
else:
    print(f"Kalan para: {kalanpara:.2f}")