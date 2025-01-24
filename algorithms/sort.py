"""Contains algorithms to sort an array"""


def bubble_sort(array: list) -> list:
    """
    Sorts and array using the bubble sort algorithm

    Arguments:-
        array(list): containing numeric values
    Returns
        array(list) - sorted array
    """
    num_elems = len(array)
    for i in range(num_elems):
        swapped = False
        for j in range(num_elems -i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped == False:
            break
    return array


def dutch_partitioning_sort(nums):
    """
    Sorts array using the dutch partitioning algorithm. Assumption is that
    input array will consist only of values 0,1,2 in any possible count and order.
    Given random array with 3 distinct numbers. Sort array such that same elements
    are together and their collective group is in the correct order.

    Arguments:
        nums(list) - array to sort
    Returns:
        nums(list) - sorted array
    """
    i, j, k = 0, 0, len(nums) - 1

    while j <= k:
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] == 1:
            j += 1
        else:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
    return nums
