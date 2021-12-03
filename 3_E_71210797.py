diamond = int(input('masukan angka :'))
a=diamond
for star in range (0,diamond):
    for pola in range (-2, a+1):
        print(' ', end='')

    for bentuk in range(0, star+1):
        print('* ', end='')
    a-=1
    print('')

a=diamond
for star in range (1, diamond):
    for pola in range (-4, star):
        print(' ',end='')

    for bentuk in range(1,a):
        print('* ',end='')
    a-=1
    print('')
