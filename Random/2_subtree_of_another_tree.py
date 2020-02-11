class Solution:
    def isSubTree(self, st, tt):
        def f(n):
            s = "(" + str(n.val)

            if n.left is None and n.right is None:
                s += "*"

            if n.left:
                s += f(n.left)
            if n.right:
                s += f(n.right)

            s += ")"
            return s
        return f(st) in f(tt)
