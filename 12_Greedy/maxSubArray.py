
def maxSubArray(a):
    ans = a[0]
    pre = 0
    for i in range(len(a)):
        pre = max(a[i], pre+a[i])
        ans = max(pre, ans)
    return ans

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))