# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def symm_tree(root):
        if root is None:
            return []
        q = deque([root])
        while q:
            width = len(q)
            for _ in range(width):
                node = q.popleft()
                if node is not None:
                    q.append(node.left)
                    q.append(node.right)
            width = len(q)
            if width %2 != 0:
                return False
            i, j = 0, width -1
            while i<j:
                if q[i] is None and q[j] is None:
                    i += 1
                    j -= 1
                    continue
                elif q[i] is None or q[j] is None:
                    return False
                if q[i].val != q[j].val:
                    return False
                i += 1
                j -= 1
        return True


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(2)
    t_root.left.left = Node(3)
    t_root.right.right = Node(3)

    print("symm_tree")

    print(t_root.symm_tree(t_root))
