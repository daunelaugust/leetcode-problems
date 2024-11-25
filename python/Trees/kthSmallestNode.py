def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    self.counts = 0
    self.rootVal = None

    def dfs(root,k):

        if root is None:
            return
        

            
        dfs(root.left,k)
        self.counts+=1
        if self.counts == k and not self.rootVal:
            self.rootVal = root.val
        elif self.rootVal:
            return
        dfs(root.right,k)
    
    dfs(root,k)
    return self.rootVal if self.rootVal else 0