def ler_numero():
    numero = int(input('Digite um numero inteiro positivo: '))
    return numero

def tabuada(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')

numero = ler_numero()
tabuada(numero)