"""
#383 Ransom Note
LeetCode #383 - Ransom Note
Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note/

Approach: Count the frequency of each character in the magazine using a hash map. 
For each character in the ransomNote, check if it exists in the map with a positive count; 
if yes, decrement the count, otherwise return False. If all characters are processed successfully, return True.
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    char_count = {}
    # Count characters in magazine
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check ransomNote
    for char in ransomNote:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    return True


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic case
    print(canConstruct("a", "b"))  # Expected: False
    
    # Test 2: Edge case
    print(canConstruct("aa", "ab"))  # Expected: False
    
    # Test 3: Another case
    print(canConstruct("aa", "aab"))  # Expected: True