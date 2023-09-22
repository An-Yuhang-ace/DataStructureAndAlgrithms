if __name__ == "__main__":
    line = input().split()
    x = int(line[0])
    while x > 0:
        n = 0
        while x >= n*(n+1)/2:
            n += 1
        n -= 1
        for i in range(n):
            print('d', end='')
        x -= n*(n+1)/2
        n = 0
        while x >= n*(n+1)/2:
            n += 1
        n -= 1
        for i in range(n):
            print('e', end='')
        x -= n*(n+1)/2
        n = 0
        while x >= n*(n+1)/2:
            n += 1
        n -= 1
        for i in range(n):
            print('r', end='')
        x -= n*(n+1)/2
    print("")
