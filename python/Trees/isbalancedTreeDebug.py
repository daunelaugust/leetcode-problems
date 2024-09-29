class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # do dfs and return sums as height upwards
        def dfs(curr):
            if not curr:
                return 0

            l = dfs(curr.left)
            r = dfs(curr.right)
            if l < 0 or r < 0:
                return -1

            if l > r:
                tmp = l - 1
                if tmp > r:
                    return -1
            else:
                tmp = r - 1
                if tmp > l:
                    return -1

            return max(l, r) + 1

        return dfs(root) >= 0
