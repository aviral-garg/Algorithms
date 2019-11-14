# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def max_width_bt(root):
        if root is None:
            return 0
        q = deque([(root, 0)])
        result = []
        while q:
            tmp = []
            num_nodes = len(q)
            for _ in range(num_nodes):
                node, i = q.popleft()
                q.append((node.left, 2*i)) if node.left is not None else None
                q.append((node.right, 2*i+1)) if node.right is not None else None
                tmp.append(i)
            result.append(tmp[-1]-tmp[0]+1)
        return max(result)


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(3)
    t_root.right = Node(2)
    t_root.left.left = Node(5)
    t_root.right.left = Node(50)
    print("max_width_bt: "+ str(t_root.max_width_bt(t_root)))

    t_root.left.left = None
    t_root.left.right = Node(5)
    print("max_width_bt: " + str(t_root.max_width_bt(t_root)))
