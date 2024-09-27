def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root:
        return None


    if root.left is None and root.right is None:
        return root
    else:
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left