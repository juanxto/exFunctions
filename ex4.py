def par_ou_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um numero: '))
if par_ou_impar(n) == True:
    print('Esse numero é par')
else:
    print('Esse numero é impar')