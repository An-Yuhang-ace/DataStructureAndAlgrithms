def firstBinarySearch(a, target):
    l, r= 0, len(a)-1
    while l <= r:
        if l == r:
            return l if a[l] == target else -1
        if l == r-1:
            if a[l] == target:
                return l
            elif a[r] == target:
                return r
            else:
                return -1
        mid = l + (r-l) // 2
        if a[mid] > target:
            r = mid - 1
        elif a[mid] < target:
            l = mid + 1
        else:
            r = mid
    return -1

def lastBinarySearch(a, target):
    l, r= 0, len(a)-1
    while l <= r:
        if l == r:
            return l if a[l] == target else -1
        if l == r-1:
            if a[r] == target:
                return r
            elif a[l] == target:
                return l
            else:
                return -1
        mid = l + (r-l) // 2
        if a[mid] > target:
            r = mid - 1
        elif a[mid] < target:
            l = mid + 1
        else:
            l = mid
    return -1


if __name__ == "__main__":
    a = [5,7,7,8,8,10]
    print(lastBinarySearch(a, 7))
