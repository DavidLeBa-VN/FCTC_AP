n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
dif = a[1] - a[0]
maxl = 0
lenht = 2
for i in range(2, n):
    if a[i] - a[i - 1] == dif:
        lenht += 1
    else:
        if(lenht > maxl):
            maxl = lenht
if (lenht > maxl):
    maxl = lenht
print(maxl)