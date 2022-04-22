cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução
valores = [[], []]
for cont in range(1, 8):
    valor = int(input(f'Digite o {az}{cont}º{li} valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-=' * 30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {am}{valores[0]}{li}')
print(f'Os valores ímpares digitados foram: {am}{valores[1]}{li}')

# Solução Gustavo Guanabara
'''
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
'''
