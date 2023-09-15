def mergeSort(a, l, r):
    if l < r:
        mid = l + (r - l) // 2
        mergeSort(a, l, mid)
        mergeSort(a, mid+1, r)
        mergeTwoSortArray(a, l, r, mid)

def mergeTwoSortArray(a, l, r, mid):
    if a[mid] <= a[mid+1]:
        return
    i = l
    j = mid + 1
    temp = []
    while i <= mid and j <= r:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
    while i <= mid:
        temp.append(a[i])
        i += 1
    while j <= r:
        temp.append(a[j])
        j += 1
    for k in range(len(temp)):
        a[k+l] = temp[k]

if __name__ == "__main__":
    a = [2, 4, 4, 1, 3, 5]
    mergeSort(a, 0, len(a)-1)
    print(a)