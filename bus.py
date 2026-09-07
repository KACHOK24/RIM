joylar = []

for i in range(1, 11):
    joylar.append(i)

while True:
    print(joylar)

    joy = int(input("Joy tanlang: "))

    if joy < 1 or joy > 10:
        print("Bunday joy yo'q!")
    elif joylar[joy - 1] == "X":
        print("Bu joy band!")
    else:
        joylar[joy - 1] = "X"
        print("Joy band qilindi!")