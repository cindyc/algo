"""Find the difference between 2 unsorted arrays
"""
arr1 = [1, 5, 6, 2]
arr2 = [2, 6, 5, 9, 10]

def diff_with_dict(arr1, arr2):
    """Use dict as storage
    """
    nums = {}
    long_arr = arr1 if len(arr1) > arr2 else arr2
    for n in arr1:
        nums[n] = 1 if n not in nums else nums[n]+1
    for n in arr2:
        nums[n] = -1 if n not in nums else nums[n]-1
    return filter(lambda x: nums[x] != 0, nums)
