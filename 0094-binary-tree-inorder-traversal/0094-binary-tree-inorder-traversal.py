# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self,root):
        r_list = []
        def inorder_list(root):
            if root is not None:
                if root.left is not None:
                    inorder_list(root.left)
                r_list.append(root.val)
                if root.right is not None:
                    inorder_list(root.right)
        inorder_list(root)
        return r_list
        
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        