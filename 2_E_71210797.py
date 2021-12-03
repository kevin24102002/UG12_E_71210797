a=str(input('Hi Tutu, Silahkan Masukan hari yang ingin anda telusuri :'))
if a == 'senin':
    pelajaran = ['kalas ke-1 Algoritma','kelas ke-3 Sistem Operasi','kelas ke-4 PAK','kelas ke-5 Pratikum Inlan']
    for isi in pelajaran :
        print(isi)
elif a == 'selasa':
    pelajaran = ['kelas ke-2 Matematika Teknik','Kelas ke-4 Bhs Indonesia','kelas ke-6 PKN']
    for isi in pelajaran :
        print(isi)
elif a =='rabu':
    pelajaran = ['Hari rabu Anda tidak ada kelas']
    for isi in pelajaran :
        print(isi)
elif a == 'kamis':
    pelajaran = ['kelas ke-1 IMK','kelas ke-3 LogMat','kelas ke-4 Pratekkom']
    for isi in pelajaran :
        print(isi)

elif a == 'jumat':
    pelajaran = ['kelas ke-2 Sistem basis data','kelas ke-4 Praktikum Sistem Basis Data','kelas ke-6 INLAN']
    for isi in pelajaran :
        print(isi)
