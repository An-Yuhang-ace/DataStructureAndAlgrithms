def heapSort(a):
    heapsize = len(a)
    buildHeap(a, heapsize)
    for i in range(len(a) - 1, 0, -1):
        swap(a, 0, i)
        heapsize -= 1
        maxHeapify(a, 0, heapsize)

def buildHeap(a, heapsize):
    p = parent(heapsize - 1)
    for i in range(p, -1, -1):
        maxHeapify(a, i, heapsize)

def maxHeapify(a, i, heapsize):
    l, r = left(i), right(i)
    largest = -1
    if l < heapsize and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, largest, i)
        maxHeapify(a, largest, heapsize)

def left(i):
    return i * 2 + 1

def right(i):
    return (i + 1) * 2

def parent(i):
    if i % 2 == 0:
        return i // 2 - 1
    else:
        return (i - 1) // 2

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == "__main__":
    a = [2, 4, 4, 1, 3, 5]
    heapSort(a)
    print(a)