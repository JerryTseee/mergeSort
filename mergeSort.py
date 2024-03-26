"""
Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays,
sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
"""

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])#add the remaining
    result.extend(left[j:])
    return result

#needs to use the recursive method
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)
    
n = [132,32,3,12,23,43,6,1]
print(mergeSort(n))