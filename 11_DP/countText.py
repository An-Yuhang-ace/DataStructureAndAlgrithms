# https://leetcode.cn/problems/count-number-of-texts/

def countText(s):
    n = len(s)
    dp3 = [0, 1, 2, 4, 7]
    dp4 = [0, 1, 2, 4, 8]
    if n > 4:
        for i in range(5, n+1):
            dp3.append(dp3[i-1] + dp3[i-2] + dp3[i-3])
            dp4.append(dp4[i-1] + dp4[i-2] + dp4[i-3] + dp4[i-4])
    if len(s) == 0:
        return 0
    ans = 1
    i, j = 0, 1
    while i < n:
        for j in range(i+1, n+1):
            if (j < n and s[j] != s[i]) or j == n:
                if s[i] == '7' or s[i] == '9':
                    ans *= dp4[j-i]
                else:
                    ans *= dp3[j-i]
                ans = ans % (10**9 + 7)
                i = j
                break
    return ans

if __name__ == "__main__":
    pressedKeys = "222222222222222222222222222222222222"
    print(countText(pressedKeys))