class Solution:
    def goLeft(self, node:Optional[TreeNode]) -> int:
        if node.left != None:
            self.goLeft(node.left)
        else:
            return node.val

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        sol = self.goLeft(root)
        return sol
