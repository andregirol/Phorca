# -*- coding: utf-8 -*-
import random

from subprocess import call
call ("clear")
call(["figlet", "-c",  "Jogo da Forca"])

# Nome de arquivo
#fname = 'wordlist.small.txt'
fname = 'wordlist.txt'
fh = open(fname)

# Cria lista para sorteio
wordlist = list(fh)


# escolhe palavra aleatoria com a biblioteca random
sorteio = random.choice(wordlist)
sorteio = sorteio.strip()

palavra = list()
for letra in sorteio:
    palavra.append(letra)

print palavra

#for line in wordlist:
#    if line == 'Abílio':
#        print "Achou!"
#        print line

#print wordlist
#for line in fh:
 #   newline = line.strip()
 #   if len(newline) <= 3:
 #       continue

    #newline = newline.lower()
    #print newline
    #print len(newline)