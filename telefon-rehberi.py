phonebook = {"Ayşe": "1234567890", "Mehmet": "0587654321", "Zeynep": "5555555555"}
name = input("isim giriniz: ")
if name in phonebook:
    print(f"{name} numarası: {phonebook[name]}")
else:    print(f"{name} rehberde bulunamadı.")