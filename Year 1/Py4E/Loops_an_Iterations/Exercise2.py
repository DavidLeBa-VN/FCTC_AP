maxi, mini, A = 0, '*', 0

while True:
    try:
        A = input('Enter a number: ')
        A = int(A)
        if mini == '*':
            mini = A
        maxi = max(A, maxi)
        mini = min(A, mini)
    except:
        if A == 'done':
            print(maxi, mini)
            break
        else:
            print('Invalid input')
