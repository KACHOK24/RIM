
matn = input("Matn kiriting: ")

alfavit = "abcdefghijklmnopqrstuvwxyz"
natija = ""

for harf in matn:
    if harf in alfavit:
        joy = alfavit.index(harf)
        natija += alfavit[joy + 1]
    else:
        natija += harf

print(natija)