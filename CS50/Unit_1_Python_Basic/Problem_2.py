s = input()
d = 0
for i in range(len(s) - 2):
    if s[i : i + 3] == 'bob':
        d += 1
print(d)