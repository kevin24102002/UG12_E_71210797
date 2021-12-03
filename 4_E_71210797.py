def nilai_a(deret_bilangan):
    nilai_besar = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai > nilai_besar:
            nilai_besar = nilai
    return nilai_besar
def nilai_b(deret_bilangan):
    nilai_kecil = deret_bilangan[0]
    for nilai in deret_bilangan :
        if nilai < nilai_kecil :
            nilai_kecil = nilai
    return nilai_kecil
a=[3, 20, 100, -35, 50]
print(a)
print('nilai terbesar:',nilai_a(a))
print('Nilai terkecil:',nilai_b(a))

b=[3, 20, 90, 35, 75]
print(b)
print('nilai terbesar:',nilai_a(b))
print('nilai terkecil:',nilai_b(b))
    
