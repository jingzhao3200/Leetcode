# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
            print(i,':', end = " ")
            print(root.val)
            i += 1
            self.display(root.left, i)
            self.display(root.right, i)



class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inIdx = inorder.index(root.val) #inIdx means in which layer down-to-up, if it is 0, means no subtree
        print(root.val, inIdx)
        print('right subtree:', inorder[inIdx+1:])
        print('left subtree', inorder[:inIdx])

        root.right = self.buildTree(inorder[inIdx+1:], postorder)
        root.left = self.buildTree(inorder[:inIdx],postorder)
        return root


def main():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder,postorder)

    #display tree
    root.display(root, 1)

    return



if __name__ == '__main__':
    main()






