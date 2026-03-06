"""
LeetCode #169 - Majority Element
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/

Problem:
Given an array nums of size n, return the element that appears
more than n // 2 times. The majority element always exists.

Approach: Boyer-Moore Voting Algorithm — maintain a candidate and a count.
When count hits 0, switch candidate to current element.
The majority element always survives since it appears > n // 2 times.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only two variables used
"""


def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic case
    print(majority_element([3, 2, 3]))              # Expected: 3

    # Test 2: Majority at the end
    print(majority_element([2, 2, 1, 1, 1, 2, 2])) # Expected: 2

    # Test 3: Single element
    print(majority_element([1]))                    # Expected: 1

    # Test 4: All same elements
    print(majority_element([7, 7, 7, 7]))           # Expected: 7