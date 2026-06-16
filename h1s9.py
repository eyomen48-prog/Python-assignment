saniye = int(input("Kaç saniye? "))

dakika = saniye // 60
kalan_saniye = saniye % 60
print(f"{saniye} saniye, {dakika} dakika ve {kalan_saniye} saniyeye eşittir.")
