# ---
# Difficulty: Medium
# Tags: [String, Two Pointers, Sliding Window, Hash Table]
# Link: https://leetcode.com/problems/permutation-in-string/description/
# ---

'''
maine permutations pdha question m aur seedhe chatgpt pe chala gya ki kya pta kuch import krna pde baaki approach toh meri clear
hi h solution m dekh hi skte ho. thodi tweaking lgi fir saare testcases bhi paas ho gye. but fir submit kiya toh 33/108 testcases
m hi crash ho gya. mai socha itni jaldi kaise code toh simple hi lg rha. turns out permutations n! hote h plus ye loop ke andar
run kr rha h aur compare kr rha h inside l2 in which is of some length 'm'. bc itni toh kbhi complexities nhi chudi damn
chatgpt keh rha this is not even factorial — which itself explodes the system and is highly impractical — chatgpt calls this:
✨factorial time (super-exponential)✨. sunke hi itna dangerous lg rha damn 💀

Time complexity: O(n! * n * m) 💀💀 = maut
Space complexity: O(n! * n) 💀 
'''

from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [''.join(p) for p in permutations(s1)]
        for i in l1:
            if i not in s2:
                continue
            else:
                return True
        return False

'''
'''
