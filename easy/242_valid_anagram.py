"""
LeetCode #242 - Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input:  s = "anagram", t = "nagaram"
Output: true

Example 2:
Input:  s = "rat", t = "car"
Output: false

Approach 1 (Sorting):
- Sort both strings and compare.
- Time Complexity:  O(m log m + n log n)
- Space Complexity: O(m + n)

Approach 2 (Hash Map / Frequency Count):
- Count characters in s and subtract counts using characters in t.
- If all counts are zero at the end, the strings are anagrams.
- Time Complexity:  O(n)
- Space Complexity: O(1) if alphabet is fixed (e.g., lowercase English letters).
"""


class Solution:
    def isAnagram_sort(self, s: str, t: str) -> bool:
        """
        Approach 1: Sort both strings and compare.
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_hash(self, s: str, t: str) -> bool:
        """
        Approach 2: Hash map / frequency count.
        """
        if len(s) != len(t):
            return False

        charCount = {}

        for ch in s:
            charCount[ch] = charCount.get(ch, 0) + 1

        for ch in t:
            charCount[ch] = charCount.get(ch, 0) - 1

        for value in charCount.values():
            if value != 0:
                return False

        return True


def solution(params):
    """
    Wrapper for local testing:

    :type params: tuple[str, str] or list[str, str]
                  params[0] = s, params[1] = t
    :rtype: bool
    """
    s, t = params
    solver = Solution()
    # You can switch between the two approaches here:
    # return solver.isAnagram_sort(s, t)
    return solver.isAnagram_hash(s, t)


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic anagram case
    print(solution(("anagram", "nagaram")))  # Expected: True

    # Test 2: Not an anagram
    print(solution(("rat", "car")))          # Expected: False

    # Test 3: Different lengths
    print(solution(("hello", "hell")))       # Expected: False

    # Test 4: Identical strings
    print(solution(("abc", "abc")))          # Expected: True

    # Test 5: Empty strings
    print(solution(("", "")))                # Expected: True
