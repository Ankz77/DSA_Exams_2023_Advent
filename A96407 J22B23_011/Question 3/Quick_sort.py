def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    pivot = unsorted_list[len(unsorted_list) // 2]
    left = [x for x in unsorted_list if x < pivot]
    middle = [x for x in unsorted_list if x == pivot]
    right = [x for x in unsorted_list if x > pivot]
    return quicksort(left) + middle + quicksort(right)

unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]
print('Quick sorted list: ',quicksort(unsorted_list))

 