class Solution:
    def __init__(self):
        self.nums = []

    def traverse(self, node: Optional[TreeNode]):
        if node.left != None:
            self.nums.append(node.left.val)
            self.traverse(node.left)
        if node.right != None:
            self.nums.append(node.right.val)
            self.traverse(node.right)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.traverse(root)
        self.nums.append(root.val)
        totalSum = 0
        for num in self.nums:
            if low <= num <= high:
                totalSum += num
        return totalSum
