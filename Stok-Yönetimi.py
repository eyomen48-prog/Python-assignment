stock = {
    "SKU1": 10,
    "SKU2": 3,
    "SKU3": 0,
    "SKU4": 7
}
kritik_stok = {key: value for key, value in stock.items() if value < 5}

print(kritik_stok)