import math
def kelilingsegitiga (daftar_koordinat, daftar_koordinat2):
    a1 = (daftar_koordinat['A'])[0]
    a2 = (daftar_koordinat['A'])[1]
    b1 = (daftar_koordinat['B'])[0]
    b2 = (daftar_koordinat['B'])[1]
    c1 = (daftar_koordinat['C'])[0]
    c2 = (daftar_koordinat['C'])[1]

    #Menghitung sisi segitga
    ab = math.sqrt((b1 - a1)**2 + (b2 - a2)**2)
    bc = math.sqrt((c1 - b1)**2 + (c2 - b2)**2)
    ac = math.sqrt((c1 - a1)**2 + (c2 - a2)**2)
   
    total_keliling = (ab + bc + ac)
    print(f'total keliling segitiga ABC adalah {total_keliling:.4f}')
    
    
    j1 = (daftar_koordinat2['J'])[0]
    j2 = (daftar_koordinat2['J'])[1]
    k1 = (daftar_koordinat2['K'])[0]
    k2 = (daftar_koordinat2['K'])[1]
    l1 = (daftar_koordinat2['L'])[0]
    l2 = (daftar_koordinat2['L'])[1]

    #Menghitung sisi segitga
    jk = math.sqrt((k1 - j1)**2 + (k2 - j2)**2)
    kl = math.sqrt((l1 - k1)**2 + (l2 - k2)**2)
    jl = math.sqrt((l1 - j1)**2 + (l2 - j2)**2)
   
    total_keliling2 = (jk + kl + jl)
    print(f'total keliling segitiga JKL adalah {total_keliling2:.4f}')

daftar_koordinat = {'A':[1,1], 'B':[5,1], 'C':[3,7]}
daftar_koordinat2 = {'J':[1,3], 'K':[4,5], 'L':[3,0]}
kelilingsegitiga(daftar_koordinat, daftar_koordinat2)  
    
    
    
    