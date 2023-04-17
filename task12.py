sum = int(input("Введите сумму: "))
count = int(input("Введите произведение: "))
p = 0
s = 0
numb = 0
for i in range(sum):
    for j in range(count):
        numb = i+j      
        if numb == count:
            p = i
            s = j
            if p * s == sum:
                print(f"Загаданы числа - {p},{s}")

        
