angka = input()
angka = int(angka)
penentu = int(angka)/2
if penentu == 1:
    print('Genap')
else:
    print('Ganjil')
def prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
if prima(angka):
    print('Prima')
else:
    print('Bukan Prima')