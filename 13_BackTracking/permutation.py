# https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/

def permutation(s):
    s = [i for i in s]
    s.sort()
    ans = []
    res = []
    used = [0 for _ in range(len(s))]
    dfs(s, 0, ans, res, used)
    return ans

def dfs(s, l, ans, res, used):
    if l == len(s):
        temp = ""
        for i in res:
            temp += i
        ans.append(temp)
        return
    
    for i in range(0, len(s)):
        if i > 0 and s[i] == s[i-1] and not used[i-1]:
            continue
        if not used[i]:
            res.append(s[i])   
            used[i] = 1
            dfs(s, l+1, ans, res, used)
            del res[-1]
            used[i] = 0

if __name__ == "__main__":
    goods = "aab"
    print(permutation(goods))