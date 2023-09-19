# https://leetcode.cn/problems/powx-n/

def myPow(x, n):
    if x == 0.0:
        return 0.0
    res = 1.0
    if n < 0:
        x = 1 / x
        n = -n
    while n > 0:
        if n % 2 == 1:
            res *= x
        x *= x
        n = n // 2
    return res

if __name__ == "__main__":
    x = 3
    n = 5
    print(myPow(x, n))
