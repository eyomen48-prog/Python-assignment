a = int(input("a: "))
b = int(input("b: "))

print(f"önce: a={a}, b={b}")
a, b = b, a
print(f"sonra: a={a}, b={b}")

