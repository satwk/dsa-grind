# ---
# Difficulty: Easy
# Tags: [Binary Tree, DFS]
# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# ---

'''
Approach:
basic question hi h binary trees ka bfs se solve kiya h using queues ofc. yahi approach rehti usually bfs binary trees m while deque then for length of deque
fir nodes ko pop krte aur uske left aur right connected nodes ko deque m daalte. Fir jo manipulation krna h question m asked vo krte h.

Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        chad = []
        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            chad.append(sum(lvl)/len(lvl))
        return chad
