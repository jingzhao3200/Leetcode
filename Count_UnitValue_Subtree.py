# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print(root.val)
        count = 0
        count1 = self.count_func(self, root, count)
        print('count1', count)
        return count

    def count_func(self, root, count):
        print(count)
        if root == None:
            print('c1')
            return

        if root.left and root.right and (root.left.val == root.right.val):
            print('c2')
            count += 1
        if root.left == None and root.right == None:
            print('c3')
            count += 1
        self.count_func(self, root.left, count)
        self.count_func(self, root.right, count)




def main():
    # testCase = [5,1,5,5,5,'null',5]
    root = TreeNode(5)
    res = Solution.countUnivalSubtrees(Solution, root)
    print(res)


    return

if __name__ == '__main__':
    main()
