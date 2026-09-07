def rim_to_son(rim):
    qiymatlar = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    natija = 0
    for i in range(len(rim)):
        joriy = qiymatlar[rim[i]]
        
        
        if i + 1 < len(rim) and qiymatlar[rim[i + 1]] > joriy:
            natija -= joriy
        else:
            natija += joriy
    
    return natija



rim_raqam = input("Rim raqamini kiriting: ").upper()
print(f"{rim_raqam} = {rim_to_son(rim_raqam)}")

