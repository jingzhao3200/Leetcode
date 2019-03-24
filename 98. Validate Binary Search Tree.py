# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isValidBST(self, root, left = float('-inf'), right = float('inf') ):
        """
        :type root: TreeNode
        :rtype: bool
        """ 
        
        if not root:
            return True
        if (left<root.val) and (root.val<right):
            return self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)

        
        
        # return not root or left < root.val < right and \
        #         self.isValidBST(root.left, left, root.val) and \
        #         self.isValidBST(root.right, root.val, right)
        
        
        
        # if not root:
        #     return True
        # if root.val <= largerThan and root.val >= lessThan:
        #     return False
        # return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and self.isValidBST(root.right, lessThan, max(largerThan, root.val))

        

        
        
#         if root is not None:
            
#             # print(root.val, root.left.val, root.right.val)
#             if root.left:
#                 if root.left.val>=root.val:
#                     return False
#             if root.right:
#                 if root.right.val<=root.val:
#                     return False
#             self.isValidBST(root.left)
#             self.isValidBST(root.right)
#             return True
#         else:
#             return True
