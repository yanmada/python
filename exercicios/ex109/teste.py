'''from ex109 import moeda

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
limpar = cores['limpar']
vermelho = cores['vermelho']
verde = cores['verde']
amarelo = cores['amarelo']

p = float(input(f'Digite o preço: {amarelo}R${limpar}'))
print(f'A metade de {moeda.moeda(p)} é {vermelho}{moeda.metade(p, False)}{limpar}')
print(f'O dobro de {moeda.moeda(p)} é {verde}{moeda.dobro(p, False)}{limpar}')
print(f'Reduzindo 13%, temos {vermelho}{moeda.diminuir(p, 13, True)}{limpar}')
print(f'Aumentando 10%, temos {verde}{moeda.aumentar(p, 10, True)}{limpar}')'''

# Solução Gustavo Guanabara

from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
