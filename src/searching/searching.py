def linear_search(arr, target):
    for i in range(len(arr)):  # what is difference between range(0, len(arr) - 1)
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid

    return -1  # not found
