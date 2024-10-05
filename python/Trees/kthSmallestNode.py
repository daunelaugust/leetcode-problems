def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    def dfs(root, k, kValues):

        if root is None:
            return

        if len(kValues) == k:
            return kValues

        left = dfs(root.left, k, kValues)
        kValues.append(root.val)
        right = dfs(root.right, k, kValues)

    values = []

    dfs(root, k, values)

    return values[k - 1] if values else 0
