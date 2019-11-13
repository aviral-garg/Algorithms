# A node structure
from collections import deque


class Node:
    # A utility function to create a new node
    def __init__(self, key, children):
        self.val = key
        self.children = children

    @staticmethod
    def n_ary_bfs(root):
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        return level


# Driver Code
if __name__ == '__main__':
    t_root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [Node(7, []), Node(8, [])])])
    print("n_ary_bfs")
    print(t_root.n_ary_bfs(t_root))
