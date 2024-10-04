class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(r, maxRoot):

            if not r:
                return 0
            
            maxRoot = max(maxRoot, r.val)
            left = dfs(r.left, maxRoot)
            right = dfs(r.right, maxRoot)

            if r.val == maxRoot:
                return 1+left+right
            else:
                return left+right

        return dfs(root, root.val)