# ---
# Difficulty: Medium
# Tags: [Arrays, Hashing, Sorting]
# Link: https://leetcode.com/problems/group-anagrams/
# ---

'''
ye pehle solution m mera thinking code dekh ke hi samajh aa jayega. bhaut hi layman-esque. maine socha ek fixed 'i' aur ek moving pointer 'j' se words leke usko list m daaldunga.
now it surely WORKS. but space time complexities chud rhi thi. suppose there are n words in strs and m is the average word length toh isme sorting storing vageira sb milake:

Time complexity: O(n^2 * mlogm) 💀 jo worst case m can tend to O(n^3) 😭. Mera Time Limit Exceeded aa gya leetcode m at 111/126 testcases
Space complexity: O(n + m) which is good but trade off is really poor
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chad = []
        i = 0
        while i < len(strs):
            j = i + 1
            k = [strs[i]]
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    k.append(strs.pop(j))
                    continue
                j += 1
            chad.append(k)
            i += 1
        return chad
      
'''
isme ofc I used help (chatgpt zindabad). defaultdict is a special type of dict by collections module in python. isme kya hota h ki:
dihh🥀 = defaultdict(default_factory)
dihh = dictionary variable
defaultdict() standard syntax h
default_factor can be list, int, set. list creates [], int creates 0, set creates empty set set(). 
iska purpose basically ye h ki
if key not in rook:
    rook[key] = [] (or 0 or set())
mtlb kaam iske bina bhi ho skta h but this makes it a tad bit easier

anyways, iss approach m for each word uska sorted version is the key which will be the same for all anagrams. suppose word is car toh uska sorted hoga 'acr'. arc ka bhi same.
toh mast approach solid 9/10. but isme ek problem h, sorted(word) function use krne se mlogm involve ho ja rha h jisse time complexity thodi si worse ho rhi h as compared to
the next approach. I mean all your testcases will still pass with this one and this looks human interviewers ko pasand aayega but from time complexity perspective, next approach
is slightly 🤏 better

Time complexity: O(n * mlogm)
Space complexity: O(n * m)
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word)) # sorting = m log m
            anagrams[key].append(word)
        return list(anagrams.values())

'''
isme poora vo upar wale ki tarah h same to same but isme sorting ka mlogm nhi ata uski jagah keval m rehta. ord() is a built in python function which returns the Unicode
Code Point (an integer) of a single character. ord('a') = 97, ord('z') = 122. dont remember, but idea ke liye bta rha hu. count ke andar ord(i)-ord('a') kiya h taki 
upar jo count = [0]*26 define kiya h usme toh jo jo alphabet word m hoga uska count utna ho jayega. example word is "scats" toh count = [1,0,1,0,0,0,....2,1,0,0,0...]
mtlb 'c' 'a' 't' ka count 1 and 's' ka count 2. also, list is not hashable toh return tuple kiya h. This is the best and the most optimised approach iss question ka but 
you just need to remember ki kaise keys lete h aur kaise hashing hoti h to solve this question again in the future. defaultdict also helps

Time complexity: O(n * m) 🤩
Space complexity: O(n * m)
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def char_count_key(word):
            count = [0]*26
            for i in word:
                count[ord(i)-ord('a')]+=1
            return tuple(count)
        anagrams = defaultdict(list)
        for word in strs:
            key = char_count_key(word)
            anagrams[key].append(word)
        return list(anagrams.values())
      
