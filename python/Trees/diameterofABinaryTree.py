class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #makes a global variable
        self.res = 0
        
        #returns height
        def dfs(curr):
            if not curr:
                return 0

            
            l = dfs(curr.left)
            r  = dfs(curr.right)

            self.res = max(self.res, l+r)
            return max(l,r)+1
        
        dfs(root)
        
        return self.res

        
