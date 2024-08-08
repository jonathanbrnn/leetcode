class Solution:
    def __init__(self):
        self.total = 0

    def traverseTree(self, root, is_left_leaf):
        if root.left is not None:
            self.traverseTree(root.left, True)
        if root.right is not None:
            self.traverseTree(root.right, False)
        if root.left is None and root.right is None and is_left_leaf:
            self.total += root.val

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.traverseTree(root, False)
        return self.total
