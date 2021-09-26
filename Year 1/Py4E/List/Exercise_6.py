a = []

while True:
    s = input('Enter a number: ')
    if s == 'done':
        break
    a.append(int(s))

print('Maximum:', max(a))
print('Minimun:', min(a))