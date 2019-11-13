# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def max_depth(root):
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return level


# Driver Code
if __name__ == '__main__':
    t_root = Node(3)
    t_root.left = Node(9)
    t_root.right = Node(20)
    t_root.right.left = Node(15)
    t_root.right.right = Node(7)

    print("max_depth")

    print(t_root.max_depth(t_root))
