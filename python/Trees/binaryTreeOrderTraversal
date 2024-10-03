class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        q = deque([root])
        res = [[root.val]]

        while q:
            
            level = []
            for i in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    level.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    q.append(curr.right)

            
            if level:
                res.append(level)
        
        return res
                