'''
Merge Sort Algorithm

In Merge Sort algorithm,
Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays,
sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
'''


def merge(list1, list2):
    combine = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combine.append(list1[i])
            i += 1
        else:
            combine.append(list2[j])
            j += 1
    while i < len(list1):
        combine.append(list1[i])
        i += 1
    while j < len(list2):
        combine.append(list2[j])
        j += 1
    return combine


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)


print(merge_sort([1, 2, 0, 8, 3]))


'''
Complexity Analysis of  Merge Sort:
Time Complexity: O(N log(N)),  Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
Auxiliary Space: O(N), In merge sort all elements are copied into an auxiliary array. So N auxiliary space is required for merge sort.
'''
