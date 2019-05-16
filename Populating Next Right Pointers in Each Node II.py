
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def display(self, root, i):
        if root is not None:
            print('level=', i,': ', end='')
            print('value=', root.val)
            i += 1
            self.display(root.left, i)
            self.display(root.right, i)

class Solution(object):
    def connect(self, node):
        """
        :type root: Node
        :rtype: Node
        """
        # prekid = kid = root
        # while root:
        #     while root:
        #         # try the left node
        #         kid.next = root.left
        #         if kid.next:
        #             kid = kid.next
        #         # try the right node
        #         kid.next = root.right
        #         if kid.next:
        #             kid = kid.next
        #         root = root.next
        #     root = prekid.next
        #     kid = prekid
        # return kid

        tail = dummy = node
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
        return node

        # if not root:
        #     return None
        # curr = root
        # next = root.left
        #
        # while curr.left:
        #     curr.left.next = curr.right
        #     if curr.next:
        #         curr.right.next = curr.next.left
        #         curr = curr.next
        #     else:
        #         curr = next
        #         next = curr.left
        # return root



def main():
    n4 = Node(4, None, None, None)
    n5 = Node(5, None, None, None)
    n2 = Node(2, n4, n5, None)

    n6 = Node(6, None, None, None)
    n7 = Node(7, None, None, None)
    n3 = Node(3, None, n7, None)

    n1 = Node(1, n2, n3, None)

    root = n1
    #display tree
    root.display(root, 1)

    sol = Solution()
    res = sol.connect(root)

    return



if __name__ == '__main__':
    main()
