count = int(input("Количество монет: "))
rewka = 0
orel = 0
for i in range(count):
    moneta = int(input("Ведите сторону монеты (Решка = 1 - Орел = -1): "))
    if moneta > 0:
        rewka+=1
    if moneta < 0:
        orel+=1
if rewka > orel:
    print(f"Нужно перевернуть орел в количестве - {orel}")
else:
    print(f"Нужно перевернуть решку в количестве - {rewka}")