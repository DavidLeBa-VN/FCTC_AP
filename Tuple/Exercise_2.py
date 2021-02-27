f = open(input('Enter a file name: '))
d = dict()

for line in f:
    if line.startswith('From') and not line.startswith('From:'):
        w = line.split()
        try:
            d[w[5][: 2]] += 1
        except:
            d[w[5][: 2]] = 1

d = dict(sorted(d.items()))

for key, val in list(d.items()):
    print(key, val)