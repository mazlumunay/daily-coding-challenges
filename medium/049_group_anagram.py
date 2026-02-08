"""
LeetCode #49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problem:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example:
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Approach (Frequency Hash Key):
- For each word, count frequency of each character (assuming 'a' to 'z'). [web:11][web:20]
- Build a hash key string from this frequency array (e.g. "1$0$0$..."). [web:11][web:13]
- Use this key in a hash map to group anagrams together. [web:11][web:20]
Time Complexity:  O(n * L + 26n) ≈ O(n * L), where n = number of words, L = max word length. [web:11][web:17]
Space Complexity: O(n * L) for storing groups and keys. [web:11][web:17]
"""

MAX_CHAR = 26

# Function to generate hash of word s
def getHash(s: str) -> str:
    hashList = []
    freq = [0] * MAX_CHAR

    # Count frequency of each character
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    # Append the frequency to construct the hash
    for i in range(MAX_CHAR):
        hashList.append(str(freq[i]))
        hashList.append("$")

    return ''.join(hashList)


def anagrams(arr):
    """
    Groups anagrams together using frequency-hash keys.

    :type arr: List[str]
    :rtype: List[List[str]]
    """
    res = []
    mp = {}

    for word in arr:
        key = getHash(word)

        # If key is not present, create a new group
        if key not in mp:
            mp[key] = len(res)
            res.append([])

        # Insert the string in its correct group
        res[mp[key]].append(word)

    return res


def solution(params):
    """
    Wrapper for local testing.

    :type params: List[str]
    :rtype: List[List[str]]
    """
    return anagrams(params)


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic case
    print(solution(["act", "god", "cat", "dog", "tac"]))
    # Expected (order may vary):
    # [["act","cat","tac"], ["god","dog"]]

    # Test 2: Example similar to LeetCode
    print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected (order may vary):
    # [["eat","tea","ate"], ["tan","nat"], ["bat"]]

    # Test 3: Edge cases (empty and single-character)
    print(solution(["", "", "a", "b", "ab", "ba"]))
    # Expected (order may vary):
    # [["",""], ["a"], ["b"], ["ab","ba"]]
