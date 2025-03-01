from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        r_degree = set()

        def dfs(node, depth,side=None):
            if not node:
                return
            if depth not in r_degree:
                res.append(node.val)
            if side == 'r':
                r_degree.add(depth)

            print(node.val)
            dfs(node.right, depth + 1,'r')
            dfs(node.left, depth + 1,'l')

            return res

        dfs(root, 0 )
        return res


