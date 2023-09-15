def maxProfit(a):
    ans = 0
    if len(a) == 0:
        return ans
    buy = a[0]
    for i in range(len(a)):
        ans = max(ans, a[i]-buy)
        buy = min(buy, a[i])
    return ans

if __name__ == "__main__":
    a = [7,1,5,3,6,4]
    print(maxProfit(a))