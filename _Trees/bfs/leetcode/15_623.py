# A node structure
from collections import deque


class TreeNode:
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
    def add_one_row(root, v, d):
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        q = deque([root])
        prev_row = []
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if level == d - 1:
                    new_node_left = TreeNode(v)
                    new_node_right = TreeNode(v)
                    new_node_left.left = node.left
                    new_node_right.right = node.right
                    node.left = new_node_left
                    node.right = new_node_right
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return root


# Driver Code
if __name__ == '__main__':
    t_root = TreeNode(1)
    t_root.left = TreeNode(2)
    t_root.right = TreeNode(3)
    t_root.left.left = TreeNode(4)
    t_root.left.right = TreeNode(5)

    print("add_one_row")

    print(t_root.bfs(t_root.add_one_row(t_root, 2, 3)))

