line = input().split()
n = int(line[0])

line = input().split()
a = [int(s) for s in line]

a.sort()
a.reverse()

for i in range(1, n):
    if a[i] & a[0] != 0:
        print([a[0], a[i]])

    print(a[0] & a[i])

cur = 1
res = []
for i in a:
    if cur & i == 0:
        res.append(i)
    cur *= 2
