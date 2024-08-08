# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def traverse(root):
            arr.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(root)

        left = 0
        right = len(arr) - 1
        arr.sort()

        while left < right:
            if arr[left] + arr[right] == k:
                return True
            elif arr[left] + arr[right] < k:
                left += 1
            else:
                right -= 1

        return False
