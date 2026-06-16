grades = [70, 45, 90, 55, 30]
total = sum(grades)
average = total / len(grades)
print(f"Not ortalaması: {average:.2f}")
if average >= 50:
    print("Sınıf geçti.")
else:
    print("Sınıf kaldı.")