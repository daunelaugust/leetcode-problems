class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        q = deque([root])
        res = []

        while q:
    
            for i in range(len(q)):
                curr = q.popleft()
                rightMost = curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(rightMost)
        
        return res