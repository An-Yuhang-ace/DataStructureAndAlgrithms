import random

def quickSort(a, l, r):
    if l < r:
        p = partition(a, l ,r)
        quickSort(a, l, p-1)
        quickSort(a, p+1, r)


def partition(a, l, r):
    p = random.randint(l, r)
    swap(a, p, r)
    j = l
    for i in range(l, r):
        if a[i] < a[r]:
            swap(a, j, i)
            j += 1
    swap(a, j, r)
    return j


def swap(a, l, r):
    temp = a[l]
    a[l] = a[r]
    a[r] = temp

if __name__ == "__main__":
    a = [2, 4, 4, 1, 3, 5]
    quickSort(a, 0, len(a)-1)
    print(a)