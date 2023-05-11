def hitung_nilai_akhir(daftar_nilai):
    for nama in daftar_nilai:
        list_nilai = []

        for nilai in daftar_nilai[nama]:
            list_nilai.append(nilai)
            list_nilai.sort(reverse= True )
        
        total = 0
        for nilai in range(n):
            total = total + list_nilai[nilai]/n

        print (f'{nama}    {total:.6f}')
        
daftar_nilai = {
'Udin': [65,74,56,80,82,94],
'Atun': [98, 88, 82, 88],
'Tejo': [85, 86]
        }

n = 2
hitung_nilai_akhir(daftar_nilai)   