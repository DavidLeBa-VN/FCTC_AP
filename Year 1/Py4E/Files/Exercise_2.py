fn = input('Enter file name: ')
f = open(fn)
cnt = 0
s = 0


for l in l:
    if not l.startswith("X-DSPAM-Confidence:"):
        continue
    num = float(l[l.find('0') :])
    cnt += 1
    s += num


print('Average spam confidence:', s / cnt)