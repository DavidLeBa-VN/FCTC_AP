a = float(input('Enter Hours: '))
b = float(input('Enter Rate: '))
if a <= 40:
    print('Pay: ', a * b)
else:
    print('Pay: ', 40 * b + (a - 40) * b * 1.5)