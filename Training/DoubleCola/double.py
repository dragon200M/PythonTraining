#!/usr/bin/python3.5

import math

def whoIsNext(names, r):

    if r > 5:
        round_floor = int(math.floor(math.log(((r + 5) / 5), 2)))

        nameIndex = math.floor((r - math.pow(2, round_floor) * 5 + 5) / math.pow(2, round_floor))

        return names[int(nameIndex)]
    else:
        return names[r-1]


