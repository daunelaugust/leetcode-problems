from typing import List, Optional

# Class definition for TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    # Create the root of the tree
    root = TreeNode(values[0])
    queue = [root]
    i = 1

    # Using a queue to iteratively build the tree
    while i < len(values):
        current = queue.pop(0)

        # Add left child if value is not None
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Add right child if value is not None
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #do dfs and return sums as height upwards
        def dfs(curr):
            if not curr:
                return 0

            l = dfs(curr.left)
            r = dfs(curr.right)

            if l>r:
                tmp = l-1
                if tmp > r:
                    return -1
            else:
                tmp= r-1
                if tmp >l:
                    return -1
            
            return max(l,r)+1

        print(dfs(root))


values = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
root = build_tree(values)

sol = Solution()
print(sol.isBalanced(root))
