"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""
import collections


# Time complexity O(n^2)
def delete_nth_naive(array, n):
    result = []
    for num in array:
        """Python List count() method returns the count of the occurrences of a given element in a list."""
        if result.count(num) < n:
            result.append(num)
    return result


# Time Complexity O(n), using hash tables.
def delete_nth(array, n):
    result = []
    """defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. 
    It provides a default value for the key that does not exists."""
    occurrences = collections.defaultdict(int)  # keep track of occurrences

    for i in array:

        if occurrences[i] < n:
            result.append(i)
            occurrences[i] += 1

    return result
