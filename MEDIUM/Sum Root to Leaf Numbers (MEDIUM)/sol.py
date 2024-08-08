# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def traverseTree(self, root, path: str):
        path1, path2 = path, path
        if root.left:
            path1 += str(root.val)
            self.traverseTree(root.left, path1)
        if root.right:
            path2 += str(root.val)
            self.traverseTree(root.right, path2)
        if root.left is None and root.right is None:
            path += str(root.val)
            self.res.append(int(path))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverseTree(root, "")
        print(self.res)
        return sum(self.res)
