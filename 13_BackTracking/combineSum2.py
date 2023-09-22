# https://leetcode.cn/problems/combination-sum-ii/

ans = []
res = []

def combinationSum2(a, target):
    a.sort()
    backtrack(a, target, 0)
    return ans

def backtrack(a, target, index):
    if target == 0:
        ans.append(res.copy())
        return 
    
    for i in range(index, len(a)):
        if i > 0 and a[i] == a[i-1] and i > index:
            # skip repeating numbers
            continue
        res.append(a[i])
        if target-a[i] >= 0:
            backtrack(a, target-a[i], i+1)
        del res[-1]


if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(combinationSum2(candidates, target))