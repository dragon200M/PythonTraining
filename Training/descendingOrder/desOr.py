#!/usr/bin/python3.5

def Descending_Order(num):
    li=list(str(num))
    li.sort(reverse=True)
    w=""
    for n in li:
        w+=n

    return int(w)



def Descending_Order2(num):
     return int("".join(sorted(str(num), reverse=True)))


def Descending_Order3(num):
    a=list(str(num))
    for i in range(len(a)-1):
     for j in range(len(a)-1):
       if int(a[j]) < int(a[j+1]):
          x = a[j]
          a[j] = a[j+1]
          a[j+1] = x

    return int("".join(a))


