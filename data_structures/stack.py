"""Contains algorithms for stack data structure."""


def next_greater_elements(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        # Remove smaller or equal elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            res[i] = stack[-1]
        
        # Push current element for future comparisons
        stack.append(arr[i])
        print(stack, res)

    return res
