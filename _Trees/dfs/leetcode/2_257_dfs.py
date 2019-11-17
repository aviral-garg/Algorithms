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
        res = []

        def dfs(node, slate):
            s = slate + "->" + \
                str(node.val) if node is not root else slate + str(node.val)
            if node.left is None and node.right is None:
                res.append(s)
            if node.left is not None:
                dfs(node.left, s)
            if node.right is not None:
                dfs(node.right, s)
        dfs(root, "")
        return res
