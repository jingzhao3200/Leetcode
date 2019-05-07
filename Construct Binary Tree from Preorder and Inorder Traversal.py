# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def display(self, root, i):
        if root is not None:
            print(i,':')
            print(root.val)
            i += 1
            self.display(root.left, i)
            self.display(root.right, i)

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            element = preorder.pop(0)
            print(element)
            root = TreeNode(element)
            nodeIdx = inorder.index(element)
            root.left = self.buildTree(preorder, inorder[0:nodeIdx])
            root.right = self.buildTree(preorder, inorder[nodeIdx+1:])
            return root


def main():
    inorder = [9, 3, 15, 20, 7]
    preorder = [3,9,20,15,7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)

    #display tree
    root.display(root, 1)

    return



if __name__ == '__main__':
    main()
