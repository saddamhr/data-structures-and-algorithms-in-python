'''
QuickSort  Algorithm

In QuickSort algorithm,
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions
the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
'''


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
    my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
    return swap_index


def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, right)
    return my_list


my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list, 0, 6))


'''
Time Complexity:

Best Case: Ω (N log (N))
The best-case scenario for quicksort occur when the pivot chosen at the each step divides the array into roughly equal halves.
In this case, the algorithm will make balanced partitions, leading to efficient Sorting.
Average Case: θ ( N log (N))
Quicksort’s average-case performance is usually very good in practice, making it one of the fastest sorting Algorithm.
Worst Case: O(N2)
The worst-case Scenario for Quicksort occur when the pivot at each step consistently results in highly unbalanced partitions. When the array is already sorted
 and the pivot is always chosen as the smallest or largest element. To mitigate the worst-case Scenario, various techniques are used such as choosing a good pivot (e.g., median of three) and using Randomized algorithm (Randomized Quicksort ) to shuffle the element before sorting.
Auxiliary Space: O(1), if we don’t consider the recursive stack space. If we consider the recursive stack space then, in the worst case quicksort could make O(N).
'''
