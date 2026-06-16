expenses = [120, 0, 75, 200, 50, 30, 90]
total_expenses = sum(expenses)
average_expense = total_expenses / len(expenses)
print(f"Toplam Harcama: {total_expenses} TL")
en_yüksek_harcama = max(expenses)
en_düşük_harcama = min(expenses)
gun = expenses.index(en_yüksek_harcama)  +1
print(f"En Yüksek Harcama: {gun}. günde: {en_yüksek_harcama}  TL")
for i in range(len(expenses)): 
    if expenses [i] == 0:
        print(f"{i+1}. günde harcama yapılmadı.")