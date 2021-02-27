n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
dif = a[1] - a[0]
for i in range(2, n):
    if a[i] - a[i - 1] != dif:
        print(False)
        exit()
print(True)
