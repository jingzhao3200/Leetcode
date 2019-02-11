# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isValSym(root.left, root.right)
        
    
    def isValSym(self, l, r):
        if l == None and r == None:
            return True
        else:
            if l and r and l.val == r.val:
                return self.isValSym(l.left, r.right) and self.isValSym(l.right, r.left)
            else:
                return False
            
    
