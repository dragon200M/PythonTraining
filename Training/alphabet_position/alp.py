#!/usr/bin/python3.5

import string

def alphabet_position(text):

    alp = list(string.ascii_lowercase)
    x = "!?.:;'"
    for char in x:
        text = text.replace(char, "")

    s = ""
    s = s.join(text.split())
    s=s.lower()

    w = list()
    for c in s:
        if c in alp:
          w.append(str(alp.index(c)+1))



    return " ".join(w)


def alphabet_position2(text):
    return ' '.join(str(ord(c)-96) for c in text.lower() if c.isalpha())



