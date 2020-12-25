sayac = 0
for x in range(102, 988):
    yuzler = str(x)[0]
    onlar = str(x)[1]
    birler = str(x)[2]

    if yuzler != onlar and yuzler != birler and onlar != birler:
        sayac = sayac+1
        print(x)

print("Rakamları birbirinden farklı sayı toplamı : "+str(sayac))