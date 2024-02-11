'''
Insertion Sort Algorithm

In Insertion Sort algorithm,
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
'''


def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([1, 4, 0, 3]))


'''
Time Complexity: O(N^2) 
Auxiliary Space: O(1) 
'''
