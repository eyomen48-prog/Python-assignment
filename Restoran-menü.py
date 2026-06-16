menu = {"Hamburger": 180, "Pizza": 220, "Ayran":30}

kdvli_menu = {}
for item, price in menu.items():
    kdvli_menu[item] = price * 1.10
print("KDV'li Menü:", kdvli_menu)