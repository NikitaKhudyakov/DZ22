count = int(input("Введите значение: "))
for i in range(count):
    v = 2**i
    if v <= count:
        x = i
print(f"степень - {x}")