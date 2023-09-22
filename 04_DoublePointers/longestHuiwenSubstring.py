# https://leetcode.cn/problems/longest-palindromic-substring/

def longestHuiwen(s):
    maxLen, index = 0, 0
    for i in range(len(s)):
        # odd
        a = expand(s, i, i)
        if a > maxLen:
            maxLen = a
            index = i
        # even
        if i + 1 < len(s) and s[i] == s[i+1]:
            a = expand(s, i, i+1)
            if a > maxLen:
                maxLen = a
                index = i
    if maxLen % 2 == 1:
        return s[index - maxLen//2: index + maxLen//2 + 1]
    else:
        return s[index - maxLen//2 + 1: index + maxLen//2 + 1]

def expand(s, i, j):
    while i >= 0 and j < len(s):
        if i > 0 and j < len(s)-1 and s[i-1] == s[j+1]:
            i -= 1
            j += 1
        else:
            break
    return j - i + 1

if __name__ == "__main__":
    s = "baabad"
    print(longestHuiwen(s))