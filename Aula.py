import random

Caracteres = 'abcdefghijklmnopABCDEFGHIJKLMNOP1234567890!@#$%&'

Tamanho = int(input('qual vai ser o tamanho da senha?'))

LetraIndesejada = input('quais caracteres voce nao quer na senha?')

Senha = ''

LetrasApagadas = 0

for i in range(Tamanho):
    Letra = random.choice(Caracteres)
    if Letra == LetraIndesejada:
        LetrasApagadas += 1
    else:
        Senha += Letra

print(Senha)