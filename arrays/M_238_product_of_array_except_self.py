# ---
# Difficulty: Medium
# Tags: [Arrays, Prefix Sum]
# Link: https://leetcode.com/problems/product-of-array-except-self/description/
# ---

'''
ye solve toh ho gya tha mere se but edge case wala 0 BT de rha tha toh usko alag se handle krna pda. fir bhi linear space time m ho gya, but question m ek followup tha jisse 
this question became a medium aur nya concept (prefix sum) seekhne ko mila. constraint neeche soln ke descprition m likha h

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        for i in nums:
            if i==0:
                continue
            pro*=i
        if 0 in nums:
            pro2 = 0
        else:
            pro2 = pro
        chad = [1]*len(nums)
        for i,v in enumerate(nums):
            if v==0:
                chad[i] = pro
            else:
                chad[i]=pro2//v
        return chad

'''
the constraint was: algo should run in O(n) and division operator must not be used. okay so O(n) wala part toh kr hi diya but division use nhi krna tha toh maine 2 loops m
products leliye: index ke left wale and index ke right wale. fir result list bnake uss index pe left*right kr diya, utna "medium"esque question nhi tha but first approach ke
baad thoda sochna pda. isme note kro ki output array (res) ki vajeh se space complexity is still O(n) but auxillary space (temporary variables, input, chhote-mote data 
structures) inka space is O(1) toh interviewer ko farak nhi pdega aur vo output array ko total space complexity m count nhi krega. nhi krna chahiye

Time complexity: O(n)
(Auxillary) Space complexity: O(1) 
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left*= nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res
