# A node structure
from collections import deque


class Node:
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


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.left.right = Node(5)

    print("Level Order Traversal of binary tree is -")

    print(t_root.bfs(t_root))
