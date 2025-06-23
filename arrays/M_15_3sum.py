# ---
# Difficulty: Medium
# Tags: [Array, Two Pointers, Sorting]
# Link: https://leetcode.com/problems/3sum/description/
# ---

'''
iska more or less smjh m aa gya concept mereko, ek element ko traverse krenge aur uske respect m left aur right pointers
move krenge and this traversal is for all the elements minus the duplicates ofc. Line 23-24 m traversal ke
time skip krne ka method h seekho. Aur line 35-36 m duplicate pointer values ko increment krne ka method h. yahi 2 cheezein
imp h iss question m baki approach toh solve krke hi pta chal gya 

Time complexity: O(n^2)
Space complexity: O(n^2) only because of the output list, this is worst case btw, if there are many triplets. 
Auxillary Space complexity: O(1) 🤩
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        chad = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left+=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    chad.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return chad
