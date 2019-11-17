# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return
        q = deque([(root, "")])
        result = []
        while q:
            level_width = len(q)
            for _ in range(level_width):
                node, slate = q.popleft()
                s = slate + "->" + \
                    str(node.val) if node is not root else slate + str(node.val)
                print(s)
                if node.left is not None:
                    q.append((node.left, s))
                if node.right is not None:
                    q.append((node.right, s))
                if node.left is None and node.right is None:
                    result.append(s)
        return result
