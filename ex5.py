import math


def area(raio):
    areaf = math.pi * raio**2
    return areaf
def perimetro(raio):
    perim = math.pi * 2 * raio
    return perim
r = float(input('Digite o raio de um circulo: '))
print(f'A area do circulo é {area(r)}')
print(f'O perimetro do circulo é {perimetro(r)}')