"""
This module contains the dutch partitioning algorithm. Given random array with 3 distinct numbers.
Sort array such that same elements are together and their collective group is in the correct order
"""

def dutch_partitioning(nums):
    """
    Sorts array using the dutch partitioning algorithm. Assumption is that
    input array will consist only of values 0,1,2 in any possible count and order.

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
