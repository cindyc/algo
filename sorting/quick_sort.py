"""
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
"""

alist = [54,26,93,17,7,31,44,55,20]


def quick_sort(alist, first, last):
    """Quick sort
    """
    if first < last:
        print "sorting: {}".format(alist[first:last+1])
        split = sort_part(alist, first, last)
        quick_sort(alist, first, split-1)
        quick_sort(alist, split+1, last)

def sort_part(alist, first, last):
    """Quick sort
    """
    pivot = alist[first]
    leftmark = first + 1
    rightmark = last
    while True:

        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark += 1
        while alist[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            break
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
     
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
