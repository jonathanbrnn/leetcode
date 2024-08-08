# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 1
        def traverse(leaf: Optional[TreeNode], steps: int):
            nonlocal res
            if leaf.left:
                traverse(leaf.left, steps + 1)
            if leaf.right:
                traverse(leaf.right, steps + 1)
            if not leaf.left and not leaf.right:
                res = max(res, steps)
        if root:
            traverse(root, 1)
        else:
            return 0
        return res
