# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            lvl_len = len(q)
            for _ in range(lvl_len):
                cur, st_min, st_max = q.popleft()
                if cur.val <= st_min or cur.val >= st_max:
                    return False
                q.append((cur.left, st_min, cur.val)) if cur.left is not None else None
                q.append((cur.right, cur.val, st_max)) if cur.right is not None else None
        return True
# T = O(N)
# S = O(N)
