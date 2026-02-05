"""
LeetCode #217 - Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Problem:
Given an integer array nums, return true if any value
appears at least twice in the array, and return false
if every element is distinct.

Approach: Use a set to track seen numbers.
If a number is already in the set, we found a duplicate.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - set stores up to n elements
"""


def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Has duplicates
    print(contains_duplicate([1, 2, 3, 1]))  # Expected: True

    # Test 2: No duplicates
    print(contains_duplicate([1, 2, 3, 4]))  # Expected: False

    # Test 3: Multiple duplicates
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Expected: True

    # Test 4: Single element
    print(contains_duplicate([1]))  # Expected: False

    # Test 5: Empty array
    print(contains_duplicate([]))  # Expected: False
