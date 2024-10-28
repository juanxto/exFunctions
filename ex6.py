def peso_ideal(altura,sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        print('Digite um valor válido')
alt = float(input('Digite a sua altura: '))
gen = input('Digite o seu genero(M para masculino e F para feminino): ')
print(f'O seu peso ideal é {peso_ideal(alt,gen)}KG')
