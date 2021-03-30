s = input()
val = ['a', 'i', 'u', 'e', 'o']
d = 0
for i in s:
    if i in val:
        d += 1
print(d)