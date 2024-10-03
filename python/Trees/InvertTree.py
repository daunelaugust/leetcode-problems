def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root:
        return None


    
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root



    