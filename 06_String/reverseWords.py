# https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/

def reverseWords(s):
    ans = ""
    s = s.strip()
    n = len(s)
    if n == 0:
        return ""
    i = n - 1
    while i >= 0:
        if s[i] == ' ':
            i -= 1
            continue
        for j in range(i - 1, -2, -1):
            if j == -1 or s[j] == ' ':
                ans += s[j + 1: i + 1] 
                i = j - 1
                ans += ' '
                break
    return ans[:-1]

if __name__ == "__main__":
    s = "a good   example"
    print(reverseWords(s))
