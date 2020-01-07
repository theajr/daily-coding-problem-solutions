"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

import collections 

def solution(numbers, k):
    temp = collections.Counter(numbers)     # Using dict to store frequency of numbers
    for n in numbers:
        diff = k-n
        if temp.has_key(diff):
            if diff == n and temp.get(n) == 1: # special case: if k=6 and there is only one 3 in the array, it should return False
                return False
            return True
    return False

assert solution([10, 15, 3, 7], 17) == True
assert solution([10, 15, 3, 3], 6) == True
assert solution([10, 15, 3, 7], 6) == False
assert solution([], 0) == False