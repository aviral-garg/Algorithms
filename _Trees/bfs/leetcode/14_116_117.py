# A node structure
from collections import deque

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.next = None

    @staticmethod
    def connect(root):
        if root is None:
            return root
        q = deque([root])
        while q:
            prev_node = None
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if prev_node is not None:
                    prev_node.next = node
                prev_node = node
        return root


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.right.right = Node(5)

    print("connect")

    t_root.connect(t_root)