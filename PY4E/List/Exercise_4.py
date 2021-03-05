fn = input('Enter file: ')
f = open(fn)
ans = []

for line in f:
    s = line.split()
    for s in s:
        if s not in ans:
            ans.append(s)

ans.sort()
print(ans)