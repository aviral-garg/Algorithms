# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def cousins_bt(root, x, y):
        if root is None:
            return False
        q = deque([root])
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                children = [node.left.val, node.right.val] if node.left is not None and node.right is not None else []
                if x in children and y in children:
                    return False
                q.append(node.left) if node.left is not None else None
                q.append(node.right) if node.right is not None else None
                tmp.append(node.val)
            if x in tmp and y in tmp:
                return True
        return False


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.left.right = Node(5)

    print("cousins_bt")

    print(t_root.cousins_bt(t_root, 4, 5))
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.left.right = Node(5)

    print("cousins_bt")

    print(t_root.cousins_bt(t_root, 4, 5))
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.right = Node(4)

    print("cousins_bt")

    print(t_root.cousins_bt(t_root, 2, 5))
