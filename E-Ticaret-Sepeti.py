cart = ["SKU1", "SKU2", "SKU1", "SKU3", "SKU2", "SKU1"]

counts = {}  # boş dict

for sku in cart:
    counts[sku] = counts.get(sku, 0) + 1

print(counts)