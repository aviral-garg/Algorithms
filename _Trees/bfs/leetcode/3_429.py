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
            return []
        q = deque([root])
        result = []
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                for c in node.children:
                    q.append(c)
                tmp.append(node.val)
            result.append(tmp)
        return result


# Driver Code
if __name__ == '__main__':
    t_root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [Node(7, []), Node(8, [])])])

    print("n_ary_bfs")

    print(t_root.n_ary_bfs(t_root))
