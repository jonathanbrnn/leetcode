# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def traverseTree(self, root):
        appended = False
        if root.left:
            if not appended:
                self.res.append(root.val)
                appended = True
            self.traverseTree(root.left)
        if root.right:
            if not appended:
                self.res.append(root.val)
                appended = True
            self.traverseTree(root.right)
        if root.left is None and root.right is None:
            self.res.append(root.val)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.traverseTree(root)
        return self.res
