from builtins import input, int, print

hora = input('Digite o horário atual: ')

try:
    hora = int(hora)

    if hora <= 11:
        print(f'Bom dia, são {hora} horas!')

    elif hora <= 17:
        print(f'Boa tarde, são {hora} horas!')
    else:
        pass

except:
    print('Valor inválido. Digite um horário entre 0 e 23. ')


