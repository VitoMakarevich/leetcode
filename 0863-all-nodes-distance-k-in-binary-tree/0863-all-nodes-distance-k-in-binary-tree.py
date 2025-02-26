# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def build_g(node):
          if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            build_g(node.left)
          if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            build_g(node.right)
        build_g(root)
        visited = set()
        cur_level = 0
        q = deque([target.val])
        while len(q) > 0 and cur_level < k:
          for i in range(len(q)):
            cur = q.popleft()
            visited.add(cur)
            for neighbor_v in graph[cur]:
              if not neighbor_v in visited:
                q.append(neighbor_v)
          cur_level += 1
        return list(q)