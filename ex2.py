def poligono(lados):
    if lados == 3:
        ptipo = 'TRIÂNGULO'
    elif lados == 4:
        ptipo = 'QUADRADO'
    elif lados == 5:
        ptipo = 'PENTÁGONO'
    else:
        ptipo = 'Valor inválido'
    return ptipo
lad = int(input('Digite o numero de lados de um poligono: '))
print(poligono(lad))