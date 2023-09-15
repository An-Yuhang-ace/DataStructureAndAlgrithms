import sys

def bubbleSort(a):
    for i in range(len(a)):
        for j in range(1, len(a) - i):
            if a[j-1] > a[j]:
                swap(a, j-1, j)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == "__main__":
    # a = [2, 4, 4, 1, 3, 5]
    # bubbleSort(a)
    # print(a)
    for line in sys.stdin:
        a = [int(s) for s in line.split()]
        bubbleSort(a)
        print(a)