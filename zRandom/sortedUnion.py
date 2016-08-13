#!/usr/bin/env python
import numpy as np

def test_sorted_union(list_1, list_2, sorted_union):
    """
    Returns true if the sorted_union is a sorted list with the
        combination of elements of list_1 and list_2 without duplicates
    :param list_1: any list with numbers in it
    :param list_2: any list with numbers in it
    :param sorted_union: a sorted list without duplicates from the other lists
    :return: (Boolean) True is sorted_union is a list without duplicates
        from list_1 and list_2, false otherwise
    """
    set_1 = set(list_1)
    set_2 = set(list_2)
    sorted_union_length_minus_1 = len(sorted_union) - 1
    i = 0
    while i < sorted_union_length_minus_1 \
            and sorted_union[i] < sorted_union[i + 1] \
            and (sorted_union[i] in set_1 or sorted_union[i] in set_2):
        i += 1
    if i == sorted_union_length_minus_1:
        return True
    else:
        return False


def sorted_union(list_1, list_2):
    """
    Returns a list that is the combination of list_1 and list_2,
        that has all unique elements and that is sorted
    :param list_1: list of numbers
    :param list_2: list of numbers
    :return: list of numbers
    """
    # checking for crazy input
    if list_1 is None and list_2 is None:
        raise Exception("both inputs cannot be None")
    if list_1 is None:
        return sorted(list_2)
    if list_2 is None:
        return sorted(list_1)

    # Now for the real sort. GO! \^v^/ <^v^>
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    union_list = []

    list_1_index = 0
    list_2_index = 0

    if sorted_list_1[list_1_index] < sorted_list_2[list_2_index]:
        union_list.append(sorted_list_1[list_1_index])
        list_1_index += 1
    elif sorted_list_1[list_1_index] > sorted_list_2[list_2_index]:
        union_list.append(sorted_list_2[list_2_index])
        list_2_index += 1
    else:  # if they are equal
        union_list.append(sorted_list_1[list_1_index])
        list_1_index += 1
        list_2_index += 1

    while list_1_index < len(sorted_list_1) and list_2_index < len(sorted_list_2):
        if sorted_list_1[list_1_index] < sorted_list_2[list_2_index]:
            if sorted_list_1[list_1_index] != union_list[-1]:
                union_list.append(sorted_list_1[list_1_index])
            list_1_index += 1
        elif sorted_list_2[list_2_index] < sorted_list_1[list_1_index]:
            if sorted_list_2[list_2_index] != union_list[-1]:
                union_list.append(sorted_list_2[list_2_index])
            list_2_index += 1
        else:  # they are equal
            if sorted_list_1[list_1_index] != union_list[-1]:
                union_list.append(sorted_list_1[list_1_index])
            list_1_index += 1
            list_2_index += 1

        if list_1_index == len(sorted_list_1):
            '''
            while list_2_index < len(sorted_list_2) \
                    and sorted_list_2[list_2_index] == union_list[-1]:
                list_2_index += 1
            '''
            for number in sorted_list_2[list_2_index:]:
                if number != union_list[-1]:
                    union_list.append(number)
            #union_list.extend(sorted_list_2[list_2_index:])
            break
        elif list_2_index == len(sorted_list_2):
            '''
            while list_1_index < len(sorted_list_1) \
                    and sorted_list_1[list_1_index] == union_list[-1]:
                list_1_index += 1
            '''
            for number in sorted_list_1[list_1_index:]:
                if number != union_list[-1]:
                    union_list.append(number)
            #union_list.extend(sorted_list_1[list_1_index:])
            break
    return union_list


'''-----------START OF SCRIPT-----------'''
'''
l1 = [9, 3, 2, 1, 4]
l2 = [7, 5, 6, 4, 1, 10, 14]

su1 = sorted_union(list_1=l1, list_2=l2)
print(su1)

was_success = test_sorted_union(list_1=l1, list_2=l2, sorted_union=su1)
success_str = "was successful" if was_success else "not successful"
print(success_str)
'''

l3 = np.random.randint(low=0, high=10, size=10)
l4 = np.random.randint(low=0, high=10, size=10)

su2 = sorted_union(list_1=l3, list_2=l4)
print("list1:\n" + str(sorted(l3)))
print("list2:\n" + str(sorted(l4)))
print("sorted:\n" + str(su2))

was_success_2 = test_sorted_union(list_1=l3, list_2=l4, sorted_union=su2)
success_str_2 = "was successful" if was_success_2 else "not successful"
print(was_success_2)