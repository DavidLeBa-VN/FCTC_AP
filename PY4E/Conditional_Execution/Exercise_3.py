a = input('Enter score: ')
try:
    a = float(a)
    if a < 0 or a > 1:
        print('Bad score')
    elif a >= 0.9:
        print('A')
    elif a >= 0.8:
        print('B')
    elif a >= 0.7:
        print('C')
    elif a >= 0.6:
        print('D')
    else:
        print('E')
except:
    print('Bad score')