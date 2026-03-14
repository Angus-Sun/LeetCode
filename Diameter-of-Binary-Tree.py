1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        self.res = 0
12        def dfs(curr):
13            if not curr:
14                return 0 
15            left = dfs(curr.left)
16            right = dfs(curr.right)
17            self.res = max(self.res, left + right)
18            return 1 + max(left, right)
19        dfs(root)
20        return self.res