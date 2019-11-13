# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    @staticmethod
    def max_lvl_sum(root):
        if root is None:
            return []
        q = deque([root])
        result = []
        while q:
            tmp = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                tmp.append(node.val)
            result.append(sum(tmp))
        return result.index(max(result))+1

    @staticmethod
    def max_lvl_sum_without_tmp_deque(root):
        if root is None:
            return []
        level = 0
        max_sum = float("-inf")
        min_level = 0
        q = deque([root])
        while q:
            level += 1
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                total += node.val
            if total > max_sum:
                max_sum = total
                min_level = level
        return min_level


# Driver Code
if __name__ == '__main__':
    t_root = Node(1)
    t_root.left = Node(7)
    t_root.right = Node(0)
    t_root.left.left = Node(7)
    t_root.left.right = Node(-8)

    print("max_lvl_sum")

    print(t_root.max_lvl_sum(t_root))
