def mediador(nota1,nota2):
    if (nota1 + nota2) / 2 < 6.0:
        res = 'Você foi reprovado'
    else:
        res = 'Você foi aprovado'
    return res
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
print(f'{mediador(n1,n2)}')