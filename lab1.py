def func_sort(arr):
    lenarr = len(arr)

    if lenarr <= 1:
        return arr

    mid = lenarr // 2

    left = func_sort(arr[:mid])
    right = func_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def dop(arr):

    arr = func_sort(arr)
    print(arr)
    result = []
    for i in arr:
        result.append(pow(i, 2))

    return func_sort(result)

arr = [5, 6, 4, 3, -5, 8, 9, 10, 7]

print(dop(arr))