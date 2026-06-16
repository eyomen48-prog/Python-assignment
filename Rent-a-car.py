rental = {"plate": "34 ABC 01", "daily": 1200, "days":3}

if rental["days"] <= 0:
    print("Hata!")
else:
    total = rental["daily"] * rental["days"]
    print(f"Total rental cost for {rental['plate']} is: {total} TL")