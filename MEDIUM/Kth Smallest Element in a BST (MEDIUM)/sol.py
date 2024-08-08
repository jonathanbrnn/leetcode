# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def traverse(root):
            arr.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(root)

        arr.sort()

        return arr[k - 1]
