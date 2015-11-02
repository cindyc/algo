"""
You are given a collection of M arrays with N integers. 
Every array is sorted. 
Develop an algorithm to combine each array into one sorted array.
"""


arrays = [
            [4, 5, 9, 19],
            [1, 6, 3, 8],
            [2, 4, 5, 6]
]


def merge_two(arr1, arr2): 
    """Merge two sorted arrays
    """
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    if i < len(arr1):
        merged += arr1[i:]
    if j < len(arr2):
        merged += arr2[j:]
    return merged

# http://www.geeksforgeeks.org/merge-k-sorted-arrays/


def quick_insert(arr, elem): 
    """Insert an elem to a sorted array
    """
    mid = len(i) / 2
    if (arr[mid] == elem or 
        (mid == 1 and arr[mid] < elem) or
        arr[mid] < elem < arr[mid+1]): 
        return mid

    elif elem < arr[mid]: 
        return quick_insert(arr[:mid], elem)
    else:
        return quick_insert(arr[mid:], elem)

def partition(arr):
    """Partition an array
    """
    mid = len(arr) / 2
    left = arr[0:mid]
    right = arr[mid:]
    return (left, right)


def merge_sort(alist): 
    """Quick sort an array
    """
    if len(alist) > 1:
        # print "arr: {}".format(alist)
        left, right = partition(alist)
        merge_sort(left)
        merge_sort(right)
        # print "Merging, left: {}, right: {}".format(left, right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        while i < len(left): 
            alist[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1
        # print "After Merged: alist: {}".format(alist)

def sort_heap(arrays, counters): 
    """Indices is a list of counters,
    counters[0] contains the current index of arrays[0]
    counters[1] contains the current index of arrays[1], and so on
    """
    alist = []
    print counters
    for i in xrange(len(counters)):
        c = counters[i]
        print "c: {}, i: {}".format(c, i)
        if counters[i] < len(arrays[0]):
            print "num: {}".format(arrays[i][c])
            alist.append((arrays[i][c], i), )
    alist.sort(key=lambda x: x[0])
    return alist


def merge_multi(arrays):
    """Merge sort M sorted arrays
    """
    merged = []
    counters = [0] * len(arrays)
    heap = [(arr[0],0) for arr in arrays]
    n = len(arrays[0])
    i = k = 0
    while True:
        print "counters: {}".format(counters)
        if counters == [n] * len(arrays):
            break
        heap = sort_heap(arrays, counters)
        min_num, min_ci = heap.pop(0)
        merged.append(min_num)
        if counters[min_ci] < n:
            counters[min_ci] += 1
    return merged

def test(): 
    arr1 = [1, 2, 4, 7, 9, 10, 30, 51, 71]
    arr2 = [2, 3, 5, 8, 11, 12, 13, 54]
    merged = merge(arr1, arr2)
