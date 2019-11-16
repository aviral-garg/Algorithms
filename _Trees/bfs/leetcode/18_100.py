# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def same_tree(p, q):
        d = deque([(p,q)])
        while d:
            lvl_len = len(d)
            for _ in range(len(d)):
                n1, n2 = d.popleft()
                if n1 is None or n2 is None:
                    if n1 is not None or n2 is not None:
                        return False
                else:
                    d.append((n1.left, n2.left))
                    d.append((n1.right, n2.right))
                    if n1.val != n2.val:
                        return False
        return True


# Driver Code
if __name__ == '__main__':
    t_root1 = Node(1)
    t_root1.left = Node(2)
    t_root1.right = Node(3)
    t_root1.left.left = Node(4)
    t_root1.left.right = Node(5)

    t_root2 = Node(1)
    t_root2.left = Node(2)
    t_root2.right = Node(3)
    t_root2.left.left = Node(4)
    t_root2.left.right = Node(5)

    print("same_tree")

    print(Node.same_tree(t_root1, t_root2))

    t_root1 = Node(1)
    t_root1.left = Node(2)
    t_root1.right = Node(3)
    t_root1.left.left = Node(4)
    t_root1.left.right = Node(7)

    t_root2 = Node(1)
    t_root2.left = Node(2)
    t_root2.right = Node(3)
    t_root2.left.left = Node(4)
    t_root2.left.right = Node(5)

    print("same_tree")

    print(Node.same_tree(t_root1, t_root2))
