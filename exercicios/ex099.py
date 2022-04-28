# Minha solução
from time import sleep
from random import randint


def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor} ', end='')
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    if len(valores) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(valores)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# Minha outra solução com números aleatórios


'''def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor} ', end='')
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    if len(valores) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(valores)}.')


maior(randint(1, 9), randint(1, 9), randint(1, 9),
      randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9))
maior(randint(1, 9))
maior()'''
