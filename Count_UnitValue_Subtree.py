import math

global count

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def countUnivalSubtrees(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         print(root.val)
#
#         sum = 0
#         self.count_func(self, root, sum)
#         return sum
#
#     # def count_func(self, root, count):
#     #     print('\ncheck count before:', count)
#     #     if root is None:
#     #         return count
#     #     else:
#     #         print('root:', root.val)
#     #         if root.left == None and root.right == None:
#     #             count += 1
#     #             print('count is:', count)
#     #             return count
#     #         else:
#     #             if root.left and root.right and (root.left.val == root.right.val):
#     #                 count += 1
#     #
#     #             count = self.count_func(self, root.left, count)
#     #             count = self.count_func(self, root.right, count)
#
#     def count_func(self, root, count):
#         print('\ncheck count before:', count)
#         if root is None:
#             return count
#         else:
#             print('root:', root.val)
#             if root.left == None and root.right == None:
#                 count += 1
#                 print('count is:', count)
#                 return count
#             else:
#                 if root.left and root.right and (root.left.val == root.right.val):
#                     count += 1
#
#                 l = self.count_func(self, root.left, count)
#                 r = self.count_func(self, root.right, count)
#                 count += (l+r)
#             return count


# # Time:  O(n)
# # Space: O(h)
# class Solution(object):
#     # @param {TreeNode} root
#     # @return {integer}
#     def countUnivalSubtrees(self, root):
#         [is_uni, count] = self.isUnivalSubtrees(self, root, 0);
#         return count;
#
#     def isUnivalSubtrees(self, root, count):
#         if not root:
#             return [True, count]
#
#         [left, count] = self.isUnivalSubtrees(self, root.left, count)
#         [right, count] = self.isUnivalSubtrees(self, root.right, count)
#         if self.isSame(self, root, root.left, left) and \
#                 self.isSame(self, root, root.right, right):
#             count += 1
#             return [True, count]
#
#         return [False, count]
#
#     def isSame(self, root, child, is_uni):
#         return not child or (is_uni and root.val == child.val)


class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.checkUni(self, root)
        return self.count

# If both children are "True" and root.val is equal to both children's values that exist,
# then root node is uniValue subtree node.
    def checkUni(self, root):
        if not root:
            return True
        l, r = self.checkUni(self, root.left), self.checkUni(self, root.right)
        if l and r and (not root.left or root.left.val == root.val) and \
        (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False

def main():
    testCase = [5,1,5,5,5,None,5]
    rootList = []
    n = len(testCase)
    # build the tree node
    for i in range(n):
        if testCase[i] != None:
            rootList.append(TreeNode(testCase[i]))
        else:
            rootList.append(None)

    n_layers = math.ceil(math.log(n, 2))
    print('n_layers', n_layers)

    #build the tree structure
    for i in range(n_layers):
        rootList[i].left = rootList[i + i + 1]
        rootList[i].right = rootList[i + i + 2]

    root = rootList[0]
    i = 0

    # print the tree
    while (root.left != None and root.right !=None and i<n):
        print(i)
        print('root: ', root.val)
        print('left: ',root.left.val)
        print('right: ',root.right.val)
        i += 1
        root = rootList[i]

    root = rootList[0]
    res = Solution.countUnivalSubtrees(Solution, root)
    print('res is', res)


    return

if __name__ == '__main__':
    main()
