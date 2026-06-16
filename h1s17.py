bölünen = int(input("Bölünen sayıyı giriniz: "))
bölen = int(input("Bölen sayıyı giriniz: "))
if bölen == 0:
    print("Bölen sıfır olamaz.")
else:
    bölüm = bölünen // bölen
    kalan = bölünen % bölen 
    print(f"Bölüm: {bölüm}")
    print(f"Kalan: {kalan}")
