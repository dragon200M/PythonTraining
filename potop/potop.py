#!/usr/bin/python3

#autor: Maciej Michalik

import re
from collections import Counter


#dokumenty
potop='potop.txt'
odm='odm.txt'



odm_plik=open(odm)

slownik_odm={}

for linia in odm_plik:
    if not linia.strip():
        continue
    else:
      lista=[]
      st=linia.strip()

      w=st.split(',')

      for slowo in w:
          lista.append(slowo.lower().strip())
      for wyraz in lista:
          slownik_odm[wyraz]=lista[0]






potop_plik=open(potop)
slownik_potop={}
lista_potop=[]
lista_zliczona=Counter()

for li in potop_plik:
    if not li.strip():
        continue
    else:

       wynik=(re.findall(r"[\w']+",li))
       for sl in wynik:
           lista_zliczona[sl.lower()]+=1



for wyra in lista_zliczona:
    if wyra in slownik_odm:
          if not slownik_odm[wyra] in slownik_potop:
            slownik_potop[slownik_odm[wyra]]=lista_zliczona[wyra]
          else:
            slownik_potop[slownik_odm[wyra]]+=lista_zliczona[wyra]


#plik do zapisu wyjścia
output = open('output.txt', 'w+')

#lista klucz:ilosc
lista_dict=[]

for klucz in slownik_potop:
    temp=[klucz,slownik_potop[klucz]]
    lista_dict.append(temp)

lista_dict.sort()



#zapis do pliku
for sl in lista_dict:
    output.write(str(sl).strip("[").strip("]").replace(',',':').replace("'","")+"\n")

output.write("\nRazem różnych wyrazów: "+str(len(lista_dict)))
#zamykamy otwarte pliki
odm_plik.close()
potop_plik.close()
output.close()
