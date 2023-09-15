def binary(a, target):
    min = 0
    max= len(a) - 1
    while min <= max:
        mid = min + (max - min) // 2
        if a[mid] > target:
            max = mid - 1
        elif a[mid] < target:
            min = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    a = [1, 4, 6, 7, 17, 20]
    print(binary(a, 18))
