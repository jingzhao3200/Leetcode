# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        # print(root.val)
        root.right = self.prev  # from most down right to up, prev is the last root, send to newroot.right, then root.left=None, give root to prev for next time 
        root.left = None
        self.prev = root
        
