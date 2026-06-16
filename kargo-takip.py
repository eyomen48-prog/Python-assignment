tracking = {"TR123": "Yolda", "TR124": "Şubede", "TR125": "Teslim Edildi"}

def update_status(tracking_code, new_status):
    eski_durum = tracking.get(tracking_code, "Yeni kayıt")
    tracking[tracking_code] = new_status
    print(f"{tracking_code}: {eski_durum} → {new_status}")

update_status("TR123", "Teslim Edildi")
update_status("TR999", "Yolda")