# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def zig_zag(root):
        if root is None:
            return []
        q = deque([root])
        result = []
        rtol = False
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                tmp.append(node.val)
            if rtol:
                tmp.reverse()
            result.append(tmp)
            rtol = not rtol
        return result

    @staticmethod
    def zig_zag_using_deque(root):
        if root is None:
            return []
        q = deque([root])
        result = []
        ltor = True
        while q:
            tmp = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if ltor:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)

            result.append(tmp)
            ltor = not ltor
        return result


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.right.right = Node(5)

    print("zig_zag")

    print(t_root.zig_zag(t_root))
