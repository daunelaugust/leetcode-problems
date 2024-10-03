class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #essentially call dfs on each of the subtree until you hit base case then add 1 to 
        # each recursion call upwards

        if root is None:
            return 0
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1