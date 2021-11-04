from builtins import print, int, input

num1 = input('Digite um número inteiro: ')

try:
    num1 = int(num1)
    if num1 % 2 == 0:
        print(f' {num1} é um número par')

    else:
        print(f' {num1} é um número impar')

except:
    print('O valor informado não é inteiro. Impossível realizar a operação com o número informado.')

