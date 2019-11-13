# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def univalued_bt(root):
        if root is None:
            return []
        q = deque([root])
        uni_val = root.val
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if node.val != uni_val:
                    return False
        return True


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.left.right = Node(5)

    print("univalued_bt")

    print(t_root.univalued_bt(t_root))
    t_root = Node(2)
    t_root.left = Node(2)
    t_root.right = Node(2)
    t_root.left.left = Node(2)
    t_root.left.right = Node(2)

    print("univalued_bt")
    print(t_root.univalued_bt(t_root))
