s = input() + "0"
sta, end = 0, 0
sn = 0
for a in range(len(s)):
    if a == 0 or s[a] < s[a - 1]:
        if (sta == end and end == 0) or (a - sn > end - sta + 1):
            sta = sn
            end = a - 1
        sn = a
print(s[sta : end + 1])