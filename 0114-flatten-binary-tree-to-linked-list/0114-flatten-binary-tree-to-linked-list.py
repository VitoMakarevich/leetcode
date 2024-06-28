# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.dig(root)
        
    def dig(self, node):
        prev_left = node.left
        prev_right = node.right
        start = node
        cur = node
        node.left = None
    
        if prev_left:
            # print(f"found left {prev_left.val} for cur {node.val}")
            nxt = self.dig(prev_left)
            # print(f"attaching {node.val} to {nxt[0].val} - left run of {node.val}")
            node.right = nxt[0]
            cur = nxt[1]

        if prev_right:
            # print(f"found right {prev_right.val} for cur {node.val}")
            nxt = self.dig(prev_right)
            # print(f"attaching {cur.val} to {nxt.val} - right run of {node.val}")
            cur.right = nxt[0]
            cur = nxt[1]

        # print(f"returning [{start.val}, {cur.val}] from {node.val}")
        return [start, cur]
        