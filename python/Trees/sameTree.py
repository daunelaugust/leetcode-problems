class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def buildTreeList(root):
            if not root:
                return None

            q = deque([root])
            res = [root.val]

            while q:

                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                        res.append(node.left.val)
                    else:
                        res.append(None)
                    if node.right:
                        q.append(node.right)
                        res.append(node.right.val)
                    else:
                        res.append(None)

            return res

        list1 = buildTreeList(p)
        list2 = buildTreeList(q)
        return list1 == list2
