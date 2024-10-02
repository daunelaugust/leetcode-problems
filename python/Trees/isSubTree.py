class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(r, s):
            if not r and not s:
                return True
            if r and s and r.val == s.val:
                return sameTree(r.left, s.left) and sameTree(r.right, s.right)
            return False

        if not subRoot:
            return True
        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
