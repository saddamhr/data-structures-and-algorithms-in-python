'''
Selection Sort Algorithm

In Selection Sort algorithm,
The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part.
This process is repeated for the remaining unsorted portion until the entire list is sorted. 
'''


def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


print(selection_sort([1, 4, 0, 3]))


'''
Complexity Analysis of Selection Sort
Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

1. One loop to select an element of Array one by one = O(N)
2. Another loop to compare that element with every other Array element = O(N)
3. Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.
The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 
'''
