# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subroot):
            if not root and subroot or not subroot and root:
                return False
            if not root and not subroot:
                return True
            return root.val == subroot.val and isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right)
        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)