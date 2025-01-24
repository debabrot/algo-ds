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


def selection_sort(array):
    """
    Sorts and array using the selection sort algorithm

    Arguments:-
        array(list): containing numeric values
    Returns
        array(list) - sorted array
    """
    num_elems = len(array)
    for i in range(num_elems):
        min_index = i
        for j in range(i+1, num_elems):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
    return array


def insertion_sort(arr):
    """
    Sorts and array using the insertion sort algorithm

    Arguments:-
        array(list): containing numeric values
    Returns
        array(list) - sorted array
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Sorts and array using the merge sort algorithm

    Arguments:-
        array(list): containing numeric values
    Returns
        array(list) - sorted array
    """
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        merge_sort(left_half)

        # Sorting the second half
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    """
    Sorts and array using the quick sort algorithm

    Arguments:-
        array(list): containing numeric values
    Returns
        array(list) - sorted array
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


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
