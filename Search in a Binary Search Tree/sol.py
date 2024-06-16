class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        found = False
        result = None

        def traverse(node, val):
            nonlocal found, result
            if node.val == val:
                found = True
                result = node
                return
            if node.left and not found:
                traverse(node.left, val)
            if node.right and not found:
                traverse(node.right, val)

        traverse(root, val)
        return result
