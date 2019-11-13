# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def min_depth(root):
        if root is None:
            return []
        q = deque([root])
        lvl = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if node.left is None and node.right is None:
                    return lvl
            lvl += 1
        return lvl  # never gets here


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.left.right = Node(5)

    print("min_depth")

    print(t_root.min_depth(t_root))
