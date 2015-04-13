# -*- coding: utf-8 -*-
import random
from subprocess import call

def banner() :
    call ("clear")
    call(["figlet", "-c", "Jogo da Forca"])
    print "\nPara sair, digite: sair"

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

# variavel para armazenar cada entrada do usuario
mascara = list()

# adiciona na mascara os underlines para o usuario preencher
for letra in palavra:

    if letra == '-':
        mascara.append("-")
    else:
        mascara.append("_")

# calcula o tamanho da palavra para dar o número de tentativas
tentativasMax = int ( len(palavra) + len(palavra)/2 )

# armazena o tamanho para mostrar ao usuário quantas letras
# possui a palavra
tamanho = str(len(palavra))

# tentativas do usuario de adivinhar a palavra
tentativas = 0
ganhou = False

while tentativas <= tentativasMax:
    # imprime o banner para o usuario
    banner()

    # print palavra
    restantes = tentativasMax - tentativas

    charRestantes = str(restantes)
    print "A palavra tem " + tamanho + " letras\n"
    print "Restam ainda " + charRestantes + " tentativas"
    print mascara
    inp = raw_input("\nEntre com uma letra:  ")
    tentativas = tentativas + 1

    # Condicoes de saida do programa

    if inp == "sair":
        break

    if len(inp) > 1:
        print "Entrada inválida!"
        continue


    i = 0
    for letra in palavra:
        if inp == letra:
            mascara[i] = inp
        i = i + 1

    if mascara.count("_") == 0:
        ganhou = True
        break

banner()
if ganhou is True:
    print "GANHOU! \o/"

else:
    print "PERDEU... :("

print "\nA palavra era: " + palavra



