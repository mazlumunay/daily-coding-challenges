"""
LeetCode #1 - Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Problem:
Given an array of integers nums and an integer target,
return indices of the two numbers that add up to target.
You may assume each input has exactly one solution,
and you may not use the same element twice.

Approach: Use a hash map to store seen numbers and their indices.
For each number, check if (target - number) exists in the map.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores up to n elements
"""



def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic case
    print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]

    # Test 2: Numbers not adjacent
    print(two_sum([3, 2, 4], 6))  # Expected: [1, 2]

    # Test 3: Same number used twice (different indices)
    print(two_sum([3, 3], 6))  # Expected: [0, 1]

    # Test 4: Negative numbers
    print(two_sum([-1, -2, -3, -4, -5], -8))  # Expected: [2, 4]
