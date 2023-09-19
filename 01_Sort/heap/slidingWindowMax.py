# https://leetcode.cn/problems/sliding-window-maximum/solutions/543426/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/

import heapq

if __name__ == "__main__":
    a = [1,3,-1,-3,5,3,6,7]
    k = 3

    window = [(-a[i],i) for i in range(k)]
    heapq.heapify(window)

    ans = [-window[0][0]]
    for i in range(k, len(a)):
        heapq.heappush(window, (-a[i], i))
        while window[0][1] <= i - k:
            heapq.heappop(window)
        ans.append(-window[0][0])

    print(ans)

