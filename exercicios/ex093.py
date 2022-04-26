cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

cadastro = {}
lgols = []
tot = 0
cadastro['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for part in range(0, quant):
    gol = int(input(f'   Quantos gols na partida {part}? '))
    lgols.append(gol)
    tot += gol
cadastro['gols'] = lgols
cadastro['total'] = tot
print('-=' * 30)
print(cadastro)
print('-=' * 30)
for chave, valor in cadastro.items():
    print(f'O campo {az}{chave}{li} tem o valor {am}{valor}{li}')
print('-=' * 30)
print(f'O jogador {am}{cadastro["nome"]}{li} jogou {az}{len(lgols)}{li} partidas.')
for pos, gol in enumerate(lgols):
    print(f'    => Na partida {az}{pos}{li}, fez {am}{gol}{li} gols.')
print(f'Foi um total de {vd}{cadastro["total"]}{li} gols.')
