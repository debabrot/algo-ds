"""Contains psuedocode to solve two pointer problems"""


class TwoPointers:
    """
    Contains psuedocode to solve two pointer problems
    """

    def __init__(self, array):
        self.array = array

    def run_from_both_ends_of_array(self):
        """
        Have 2 pointers at left and right end of the array.
        Then move them to the center while processing something
        with them.
        """
        start = 0
        end = len(Self.array)
        condition = True
        
        while start != end:
            if condition:
                return [start, end]
            else:
                if condition greater:
                    end -= 1
                else:
                    start += 1

