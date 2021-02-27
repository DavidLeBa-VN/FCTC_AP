n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(1, n):
    if lst[i] > lst[i - 1]:
        print(False)
        exit()
print(True)