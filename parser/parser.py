#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Nome de arquivo
filename = 'wordlist.new.3.txt'
outputfile = 'wordlist.4.acentos.txt'
fh = open(filename)

acentos = "ãáàâêèéíôóú"
acentuado = False
for line in fh:
    for letra in line:
        if letra in acentos:
            acentuado = True

    newline = line.strip()

    if acentuado is True:
        acentuado = False
        continue

    if len(newline) > 10:
        continue
    if '-' in line:
        continue
    newlist = open(outputfile,'a')
    newlist.write(line)

#f = open('wordlist.new.txt','w')
#f.write('hi there\n') # python will convert \n to os.linesep
#f.write('hello again!\n')
#f.close()




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