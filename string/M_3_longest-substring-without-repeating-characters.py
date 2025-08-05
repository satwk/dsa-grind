# ---
# Difficulty: Medium
# Tags: [String, Sliding Window]
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# ---

'''
maine ye question kr rkha tha stoney ke approach se but revisit krte time I couldn't recall. toh maine abhi neetcode wale approach
se kiya h which incorporates two pointers to implement a sliding window. its cool and simple. isse rattne ki zrurat nhi h 
bs smjh jao how left and right pointers work, kaise removal ho rha aur kiska max le rhe

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in Set:
                Set.remove(s[left])
                left+=1
            Set.add(s[right])
            result = max(result, right - left + 1)
        return result
