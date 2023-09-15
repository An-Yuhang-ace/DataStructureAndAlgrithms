def findContinuousSequence(target):
    ans = []
    i, j = 1, 2
    while i < j:
        sum = (i + j) * (j - i + 1) / 2
        if sum < target:
            j += 1
        elif sum > target:
            i += 1
        else:
            res = []
            for k in range(i, j+1):
                res.append(k)
            ans.append(res)
            i += 1
    return ans


if __name__ == "__main__":
    print(findContinuousSequence(9))