#!/usr/bin/python3

#autor Maciej Michalik

import string
import sys
from collections import Counter
from operator import itemgetter


def zliczanie(zdanie,N,slownik):
    zlen=len(zdanie)
    k=0
    zd=Counter()
    while(k<zlen-N+1):
        zd[zdanie[k:k+N].replace("\n"," ").lower()]+=1
        k=k+1


    licznik=0


    for gram in zd:
        if gram in slownik:
            licznik+=zd[gram]*slownik[gram]

    mianownik=0
    for gram in zd:
        mianownik+=zd[gram]**2

    return licznik/mianownik


#end_def

def jezyk(polski,angielski):

    if polski > angielski:
        return "Zdanie jest w języku polskim."
    if angielski > polski:
        return "Zdanie jest w języku angielskim."
#end_def

def ngram(plik,N):

    f = open(plik, 'r')


    ln = f.read()
    slownik=Counter()
    wlen = len(ln)
    i = 0
    while (i < wlen-N+1):
      slownik[ln[i:i+N].replace("\n"," ").lower()]+=1
      i = i + 1

    f.close()

    return slownik

#end_def

pol=ngram('hp_pol.txt',3)
ang=ngram('hp_ang.txt',3)



zdanie="""Not for the first time, an argument had broken out over breakfast at number four, Privet Drive.
Mr. Vernon Dursley had been woken in the early hours of the morning by a loud,
hooting noise from his nephew Harry's room."""

polski=zliczanie(zdanie,3,pol)
angielski=zliczanie(zdanie,3,ang)

print(jezyk(polski,angielski))


zdanie2="""Nie po raz pierwszy w domu przy Privet Drive numer cztery śniadanie przerwała awantura. Wczesnym rankiem pana Dursleya obudziło głośne bębnienie dochodzące z pokoju jego siostrzeńca Harryego.
- To już trzeci raz w tym tygodniu! - ryknął na niego poprzez stół. - Jeśli nie potrafisz zapanować nad tą sową, będziesz się musiał z nią pożegnać!
Harry jeszcze raz spróbował to wyjaśnić."""

polski2=zliczanie(zdanie2,3,pol)
angielski2=zliczanie(zdanie2,3,ang)

print(jezyk(polski2,angielski2))
