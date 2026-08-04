import random

def senha():
    Caracteres = 'abcdefghijklmnopABCDEFGHIJKLMNOP1234567890!@#$%&*_=?'
    Tamanho = int(12)
    Senha = ''
    for i in range(Tamanho):
        Letra = random.choice(Caracteres)
        Senha += Letra
    return Senha
