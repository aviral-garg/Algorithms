# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def isCompleteTree(root):
        if root is None:
            return False
        q = deque([(root, 1)])
        exp_id = 1
        while q:
            cur, i = q.popleft()
            if i == exp_id:
                exp_id += 1
            else:
                return
            q.append((cur.left, 2 * i)) if cur.left is not None else None
            q.append((cur.right, 2 * i + 1)) if cur.right is not None else None
        return True

    @staticmethod
    def isCompleteTree2(root):
        if root is None:
            return False
        q = [root]
        i=0
        while q[i]:
            q.append(q[i].left)
            q.append(q[i].right)
            i+=1
        return not any(q[i:])


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(2)
    t_root.right = Node(3)
    t_root.left.left = Node(4)
    t_root.left.right = Node(5)

    print("isCompleteTree")

    print(t_root.isCompleteTree(t_root))
