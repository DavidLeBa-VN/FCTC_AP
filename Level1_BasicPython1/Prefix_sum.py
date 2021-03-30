n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = []; s = 0
for i in range(n):
    s += a[i]
    b.append(s)
print(b)