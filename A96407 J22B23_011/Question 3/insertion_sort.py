def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        current_value = unsorted_list[index]
        position = index

        while position > 0 and unsorted_list[position - 1] > current_value:
            unsorted_list[position] = unsorted_list[position - 1]
            position = position - 1

        unsorted_list[position] = current_value

    return unsorted_list

unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]
sorted_list = insertion_sort(unsorted_list)
print('Insertion sorted list: ',sorted_list)

