'''
Bubble Sort Algorithm

In Bubble Sort algorithm,
1. traverse from left and compare adjacent elements and the higher one is placed at right side. 
2. In this way, the largest element is moved to the rightmost end at first. 
3. This process is then continued to find the second largest and place it and so on until the data is sorted.
'''

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


print(bubble_sort([1, 4, 0, 3]))


'''
Complexity Analysis of Bubble Sort:
Time Complexity: O(N2)
Auxiliary Space: O(1)
'''
