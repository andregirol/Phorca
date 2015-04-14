#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from subprocess import call

# banner com a logo
def banner() :
    call ("clear")
    call(["figlet", "-c", "Jogo da Forca"])


# Nome de arquivo
#fname = 'wordlist.small.txt'
fname = 'wordlist.txt'
fh = open(fname)

# Cria lista para sorteio a partir do arquivo
wordlist = list(fh)

# escolhe palavra aleatoria com a biblioteca random
palavra = random.choice(wordlist)

# remove espaços no final do arquivo
palavra = palavra.strip()

#transforma em lowercase
palavra = palavra.lower()

# armazena as letras que o usuário já digitou
entradas = list()

# variavel para armazenar cada entrada do usuario
mascara = list()

# adiciona na mascara os underlines para o usuario preencher
for letra in palavra:
    mascara.append("_")

# calcula o tamanho da palavra para dar o número de tentativas
tentativasMax = int ( len(palavra) + len(palavra)/2 )

# armazena o tamanho em char para mostrar ao usuário quantas letras
# possui a palavra
tamanho = str(len(palavra))

# tentativas do usuario de adivinhar a palavra
tentativas = 0
ganhou = False

while tentativas < tentativasMax:

    # imprime o banner para o usuario
    banner()

    # testa se o usuário ganhou o jogo
    if mascara.count("_") == 0:
        ganhou = True
        break

    restantes = tentativasMax - tentativas

    # Converte as tentativas em char para mostrar ao usuario
    charRestantes = str(restantes)
    print ('Para sair, digite: sair')
    print ("A palavra tem ", tamanho, "letras\n")
    print ("Restam ainda ", charRestantes , "tentativas")

    # o * imprime a máscara sem os '_'
    print (*mascara)
    inp = input("\nEntre com uma letra:  ")

    if inp in entradas:
        var = input("\nLetra já digitada, tente outra.\n\nDigite ENTER para continuar...")
        continue
    else:
        entradas.append(inp)


    # Condicoes de saida do programa
    if inp == "sair":
        break

    if len(inp) > 1:
        print ("Entrada inválida!")
        continue

    i = 0
    for letra in palavra:
        if inp == letra:
            mascara[i] = inp
        i = i + 1

    tentativas = tentativas + 1

banner()
if ganhou is True:
    print ("\n\nGANHOU! \o/")

else:
    print ("\n\nPERDEU... :(")

print ("\nA palavra era: ",palavra)



