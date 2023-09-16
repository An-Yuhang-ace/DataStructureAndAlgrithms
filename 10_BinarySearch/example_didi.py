def binarySearch(k, a):
    # O(log(a[-1])*len(a))
    a.sort()
    start = a[0]
    end = a[-1]
    while start <= end:
        # mid is the maxLen in this loop
        mid = start + (end - start) // 2

        # check if mid meets the requirement
        count = 1
        last = a[0]
        for i in range(1, len(a)):
            if a[i] - last >= mid:
                count += 1
                last = a[i]
        
        # if mid does, increase
        # else, decrease
        if count >= k:
            start = mid + 1
        else:
            end = mid - 1
    return end

if __name__ == "__main__":
    n, k = map(int, input().split())
    line = input().split()
    a = [int(s) for s in line]
    print(binarySearch(k, a))