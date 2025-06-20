# ---
# Difficulty: Medium
# Tags: [Arrays, Hashing, Bucket Sort]
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# ---

'''
ye question maine ofc help se pehle kr rkha tha when I retried it while solving neetcode 150 I couldn't recall the approach toh ye bs aise hi h brute force hi maanlo
koi data structure as such use nhi hua isme other than dihh for hashing the elements. moral, dont just submit solutions leetcode pe for the sake of get a green box,
actually smjho then only post submissions. also, keep revising shit

Time complexity: O(n^2)
Space complextiy: O(n)
'''

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dihh = defaultdict(int)
        for i in nums:
            dihh[i]+=1
        chad = []
        while k!=0:
            maxval = maxkey = 0
            for kk,vv in dihh.items():
                if vv>maxval:
                    maxval = vv
                    maxkey = kk
            chad.append(maxkey)
            dihh.pop(maxkey)
            k-=1
        return chad
      
'''
Isme ek nya use hua h bucket sort. basically jaise nums = [4,5,5,6,6,6] toh bucket sort wale part se kya hoga ki ek list create ho jayegi whose elements
themselves are empty lists and this main list is of length = nums. this main list signifies the elements' frequencies. toh for nums, freq list will be [[4],[5],[6],[],[],[]]
mtlb jaise agar [4,4,5,5,6,6,6] hota toh [[],[4,5],[6],[],[],[]] hota mtlb 4 aur 5 dono ki frequency 2 hai isiliye vo freq list ke 2nd elements h ykwim?

I'll link the neetcode vid jisse seekha maine ye https://www.youtube.com/watch?v=YPTqKIgVk-k bhaut acche se visualise krwaya isse Navdeep bhai ne.
abhi bhi nhi smjha toh just search up "bucket sort visualisation" and watch top 2-3 vids, g4g ka ek 2 min ka vid h which
is nice aswell. iss question m bucket sort hi main tha ye yaad rkhna

Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i]+=1
        #bucket sort start
        freq = [[] for i in range(len(nums)+1)]
        for kk,vv in count.items():
            freq[vv].append(kk)
        #bucket sort end
        result = []
        for i in range(len(freq)-1,0,-1):
            for element in freq[i]:
                result.append(element)
                if len(result)==k:
                    return result
