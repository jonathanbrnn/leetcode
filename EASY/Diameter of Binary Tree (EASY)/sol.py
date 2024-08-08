class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = [0]

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            diameter[0] = max(diameter[0], left + right)

            return max(left, right) + 1

        helper(root)
        return diameter[0]
