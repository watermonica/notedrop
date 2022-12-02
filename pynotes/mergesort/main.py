# Merge Sort
arr = list(map(int, input().split(' ')))


def mergesort(x):
    arr1, arr2 = sorted(x[:int(len(x)/2)]), sorted(x[int(len(x)/2):])
    master = [0] * 8
    i, j = 0, 0

    # merge sort algorithm
    for _ in range(len(x)):
        if _ < 7:
            if arr1[i] < arr2[j]:
                master[_] = arr1[i]
                if i <= 3:
                    i += 1
                continue
            elif arr1[i] > arr2[j]:
                master[_] = arr2[j]
                if j < 3:
                    j += 1
                continue
        if _ >= 7:
            if arr[i] > arr2[j]:
                master[_] = arr1[i]
            else:
                master[_] = arr2[j]
    return master


if __name__ == '__main__':
    print(mergesort(arr))
