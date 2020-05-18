# TO-DO: Complete the selection_sort() function below
# test example: array [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):

    # loop through n-1 elements
    # for every iteration, the minimum element from unsorted subarray is picked and moved to the sorted subarray
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # Your code here
        # finding the minimum element in remaining unsorted array
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

# test example: array [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# round 1:
# 1 is considered sorted, rest are considered unsorted ( 1 = cur_index )
# 1 is the minimum ( smallest_index = cur_index )
# 1 (arr[smallest_index]) < 5 (arr[j]) so nothing happens ( for j in range( 5 - 7 ))
# 1 < 8 nothing happens
# etc... until 0
# 0 (arr[j]) < 1 (arr[smallest_index]) so 0 is new minimum ( smallest_index = j )
# 0 > 3 so do nothing
# 0 > 7 so do nothing
# swap 1 and 0
# array is now [0, 5, 8, 4, 2, 9, 6, 1, 3, 7]

# round 2:
# 5 is the minimum
# 5 > 8 so nothing happens
# 4 < 5 so 4 is new minimum
# 4 > 2 so 2 is new minimum
# 2 < 9 nothing happens
# 2 < 6 nothign happens
# 2 > 1 so 1 is new minimum
# 1 < 3 so do nothing
# 1 < 7 so do nothing
# swap 1 and 5
# array is now [0, 1, 8, 4, 2, 9, 6, 5, 3, 7]

# round 3:
# 8 is the minimum
# 4 < 8 so 4 is new minimum
# 2 < 4 so 2 is new minumum
# 2 < rest of elements so do nothing
# swap 2 and 8
# # array is now [0, 1, 2, 4, 8, 9, 6, 5, 3, 7]

# etc until whole array is sorted


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # outer loop
    # start range at length of the arr - 1 to 0 in negative order so -1
    # for i in range(len(arr)-1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]

    # return arr

    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                # if item in the list to the left is greater than the item to the right then sorted is false, once done the sorted on line 77 remains true which breaks out of the loop
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
