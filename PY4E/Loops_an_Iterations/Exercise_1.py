N, S, A = 0, 0, 0

while True:
    try:
        A = input('Enter a number: ')
        A = int(A)
        S += A
        N += 1
    except:
        if A == 'done':
            print(S, N, S / N)
            break
        else:
            print('Invalid input')
