# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.deleteNode(root.left, key)
        right = self.deleteNode(root.right, key)

        #searching key
        if key == root.val:
            if not root.left and not root.right: #no child
                return None
            if not root.left:      #1 right child
                return root.right
            if not root.right:     #1 left child
                return root.left

            #2 child
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val 
                root.right = self.deleteNode(root.right, root.val)

        if key < root.val:   #traversing
            root.left = left
            
        elif key > root.val:
            root.right = right
   

        return root

