# ---
# Difficulty: Easy
# Tags: [Tree, Binary Tree, Recursion]
# Link: https://leetcode.com/problems/same-tree/description/
# ---

'''
neetcode ki approach h, pehle check kiya if both p and q are null. agar both null mtlb both equal so true
fir check kiya ki "if p null or q null" mtlb dono m se ek null hoga aur doosre ki kuch value hogi which means they are not
equal i.e. return false. fir unki value check ki
isko recursively har node ke liye kar diya, neeche ka return statement is the most important thing isme kyuki recursion ka
sochna mere se nhi hua tha mai deque se dfs kr rha tha, although ho usse bhi jayega but ye approach is easy peasy and zyada
brain-power nhi lgri

Time complexity: O(n)
Space complexity: O(1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
