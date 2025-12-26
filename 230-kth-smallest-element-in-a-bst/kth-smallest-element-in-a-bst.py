# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def helper(node):
            if not node or self.result is not None:
                return None

            # inorder
            helper(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            helper(node.right)

        helper(root)
        return self.result
