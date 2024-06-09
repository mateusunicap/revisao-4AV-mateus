# 1)Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(* numeros):
    maior_elemento = numeros[0]
    for i in range(1, len(numeros)):
        maior_elemento = numeros[i]
    print(maior_elemento)


maior(1, 2, 3, 4)
maior(100, 2)

print('Hello World')
