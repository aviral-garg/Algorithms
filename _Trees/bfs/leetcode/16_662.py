# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def bfs(root):
        if root is None:
            return []
        q = deque([root])
        result = []
        while q:
            tmp = []  # or `tmp = deque()` for appendleft()
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                tmp.append(node.val)
            result.append(tmp)
        return result

    @staticmethod
    def max_width_bt(root):
        pass


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(3)
    t_root.right = Node(2)
    t_root.left.left = Node(5)

    print("max_width_bt")

    print(t_root.max_width_bt(t_root))
