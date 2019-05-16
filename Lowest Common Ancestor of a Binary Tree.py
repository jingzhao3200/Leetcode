'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def display(self, root, i):
        if root is not None:
            print('level=', i,': ', end='')
            print('value=', root.val)
            i += 1
            self.display(root.left, i)
            self.display(root.right, i)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

def main():
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2 = TreeNode(2)

    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n3 = TreeNode(3)

    n1 = TreeNode(1)

    root = n1
    #display tree
    root.display(root, 1)

    sol = Solution()
    res = sol.lowestCommonAncestor(root, None, None)

    return



if __name__ == '__main__':
    main()
