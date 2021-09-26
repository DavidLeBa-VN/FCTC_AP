fn = input('Enter a file name: ')
f = open(fn)
n = 0
for line in f:
    if not line.startswith('From'):
        continue
    n += 1
    s = line.split()
    print(s[1])

if n == 1:
    print('There was 1 lines in the file with From as the first word')
else:
    print('There were', n, 'lines in the file with From as the first word')