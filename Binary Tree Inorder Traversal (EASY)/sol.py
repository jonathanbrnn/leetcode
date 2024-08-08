class Solution:
    def __init__(self):
        self.res = []

    def traverseTree(self, root):
        if root:
            self.traverseTree(root.left)
            self.res.append(root.val)
            self.traverseTree(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverseTree(root)
        return self.res
        return self.res
