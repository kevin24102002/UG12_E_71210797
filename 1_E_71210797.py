a = int(input('masukan awal deret:'))
b = int(input('masukan akhir deret:'))
for x in range(a,b):
    if x % 2 == 0 and x % 5  != 0 and x % 9 != 0:
        print(x, end=' ')
    
    
    
