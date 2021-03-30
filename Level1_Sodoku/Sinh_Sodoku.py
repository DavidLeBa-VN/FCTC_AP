import random

lstans = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def update(hang, vitri, giatri):
    for i in range(1, 10):
        if(lstans[hang][i] == 0):
            vitri -= 1
        if(vitri == 0):
            lstans[hang][i] = giatri
            return

for i in range(1, 10):
    for j in range(1, 10):
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for vtr in range(1, 10):
            lst[lstans[i][vtr]] = 0
            lst[lstans[vtr][j]] = 0
        v = 0
        while (v < len(lst)):
            if(lst[v] == 0):
                del lst[v]
            else:
                v += 1
        if len(lst) > 0:
            k = random.choice(lst)
            lstans[i][j] = k

for i in range(1, 10):
    for j in range(1, 10):
        print(lstans[i][j], end = " ")
    print("")

