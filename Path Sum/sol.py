# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.currentPathSum = 0

    def traverseAllPaths(self, leaf, targetSum):
        if leaf is None:
            return False

        self.currentPathSum += leaf.val

        if leaf.left is None and leaf.right is None:
            if self.currentPathSum == targetSum:
                return True
        else:
            if self.traverseAllPaths(leaf.left, targetSum):
                return True
            if self.traverseAllPaths(leaf.right, targetSum):
                return True

        self.currentPathSum -= leaf.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.traverseAllPaths(root, targetSum)