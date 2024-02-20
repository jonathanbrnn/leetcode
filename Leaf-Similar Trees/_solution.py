# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self, node: Optional[TreeNode], nums: list) -> list:
        if node is None:
            return
        if node.left is None and node.right is None:
            nums.append(node.val)
            print(node.val)
        else:
            if node.left is not None:
                self.traverse(node.left, nums)
            if node.right is not None:
                self.traverse(node.right, nums)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []
        self.traverse(root1, r1)
        self.traverse(root2, r2)

        if r1 == r2:
            return True
        else:
            return False
