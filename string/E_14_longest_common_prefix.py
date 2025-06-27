# ---
# Difficulty: Easy
# Tags: [String]
# Link: https://leetcode.com/problems/longest-common-prefix/description/
# ---

'''
isme edge cases handle krne baad code logical lg rha tha but try except maine first time use kiya isme toh hua kya:
suppose testcase = ["ab","a"] toh isme the outer while will run but nested while loop ki condition m hi error aajayega
and flow will exit before reaching/updating minpref toh wrong answer aajayega. but a good brute force approach nonetheless.
socha toh sahi

Time complexity: O(S) S is the sum of characters compared jaise len(flower)=6, flow=4, flight=6 so S = sum = 16
Space complexity: O(1)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        minpref = float('inf')
        i = 1
        while i<len(strs):
            prefix = 0
            try:
                while strs[i][prefix]==strs[i-1][prefix]:
                    prefix+=1
                minpref = min(minpref, prefix)
            except:
                pass
            i+=1
        if minpref==float('inf'):
            return strs[0]
        return strs[0][:minpref] 

'''
iss wale m try except ko ditch krdiya maine aur inner while ki condition m hi check krliya the element's length jisse error
ka scope hi na ho, toh isse answer toh aaja rha h. mtlb correct h ye. but leetcode pe it says "beats only 5%" mtlb mera
code abhi bhi optimised nhi h

Time complexity: O(S)
Space complexity: O(1)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        if len(strs)==1:
            return strs[0]
        minpref = float('inf')
        i = 1
        while i<len(strs):
            prefix = 0
            while (prefix<len(strs[i-1])) and (prefix<len(strs[i])) and (strs[i][prefix]==strs[i-1][prefix]):
                prefix+=1
            minpref = min(minpref, prefix)
            if minpref==0:
                return ""
            i+=1
        
        return strs[0][:minpref] 

'''
ye code chatgpt zindabaad because I didnt even know ki python m startswith() krke ek inbuilt function h 🤦🏽‍♀️
isme first element ko hi prefix set krdete jaise maanlo flower h toh fir wo index 1 se for loop m check krega
what while loop does is, jaise does "flow" start with "flower"? No ofc. then new prefix = prefix[:-1] mtlb new prefix
is "flowe" again No. new pref is "flow" now yes. aise chalta ye. at any point if the prefix becomes "", the flow exits early
by just returning "".

n = number of elements
m = worst case scenario where shortest prefix is an element of size m

Space complexity: O(m)
Time complexity: O(n*m^2) ??? this beats 100% on leetcode so this quadratic looking is somehow more optimised than a O(S) which
from the looks of it seems linear??
pehle dekho n*m^2 kaise. for each of n-1 strings the startswith() can be called upto 'm' times and this compares atmost 'm' 
characters isiliye m^2 and n cuz n elements

chatgpt ne bhaut acche se explain kiya h I'll add it end m
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if prefix=="":
                    return ""
        return prefix

'''
In practice, an O(n*m^2) solution can outperform an O(S) because real inputs often cause the prefix to shrink quickly, 
drastically reducing the number of comparisons, and because operations like Python’s built-in startswith() are highly optimized
at a low level (C language 😜😜). Meanwhile, the theoretical O(S) approach, while linear in total input size, may involve more
Python-level overhead with character-by-character comparisons and checks, leading to slower runtime on typical test cases
despite its better worst-case complexity. So, practical runtime depends heavily on input characteristics and implementation 
details, not just big-O.

Thank you chatgpt. Very cool 😃👍
'''
