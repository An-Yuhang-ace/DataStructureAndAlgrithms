import sys

def lengthOfLongestSubstring(s):
    occ = set()
    if len(s) == 0:
        return 0
    i, j = 0, 0
    ans = j-i+1
    for j in range(len(s)):
        if s[j] not in occ:
            occ.add(s[j])
        else:
            while i < len(s) and s[i] != s[j]:
                occ.remove(s[i])
                i += 1
            i += 1
        ans = max(ans, j-i+1)
    return ans


if __name__ == "__main__":
    # s = "abcabcbb"
    # print(lengthOfLongestSubstring(s))
    for line in sys.stdin:
        print(lengthOfLongestSubstring(line))