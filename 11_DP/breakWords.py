def breakWords(s, wordDict):
    n = len(s)
    wordDict.sort()

    dp = [False for i in range(n+1)]
    dp[0] = True
    for i in range(0, n):
        for word in wordDict:
            is_match = 1
            for j in range(len(word)):
                if i+j >= n or s[i+j] != word[j]:
                    is_match = 0
                    break
            if is_match and dp[i] == True:
                dp[i+len(word)] =  True
    return dp[n]

if __name__ == "__main__":
    s = "bb"
    wordDict = ["a","b","bbb","bbbb"]
    print(breakWords(s, wordDict))