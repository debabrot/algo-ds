"""Tests sorting algorithms"""

from algorithms.sort import bubble_sort, dutch_partitioning_sort, \
    selection_sort, insertion_sort, merge_sort, quick_sort, pancake_sort


def test_bubble_sort():
    input_array = [6,5,4,3]
    expected_result = [3,4,5,6]
    result = bubble_sort(input_array)
    assert result == expected_result


def test_selection_sort():
    input_array = [6,5,4,3]
    expected_result = [3,4,5,6]
    result = selection_sort(input_array)
    assert result == expected_result


def test_insertion_sort():
    input_array = [6,5,4,3]
    expected_result = [3,4,5,6]
    result = insertion_sort(input_array)
    assert result == expected_result


def test_merge_sort():
    input_array = [6,5,4,3]
    expected_result = [3,4,5,6]
    result = merge_sort(input_array)
    assert result == expected_result


def test_quick_sort():
    input_array = [6,5,4,3]
    expected_result = [3,4,5,6]
    result = quick_sort(input_array)
    assert result == expected_result


def test_dutch_partitioning_sort():
    input_array = [2,2,1,1,0,0]
    expected_result = [0, 0, 1, 1, 2, 2]
    result = dutch_partitioning_sort(input_array)
    assert result == expected_result


def test_pancake_sort():
    input_array = [6,5,4,3]
    expected_result = [3,4,5,6]
    result = pancake_sort(input_array)
    assert result == expected_result
