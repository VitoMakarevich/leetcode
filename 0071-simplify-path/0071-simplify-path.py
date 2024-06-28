from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        q = deque()
        identifiers = filter(lambda x: x != '.' and len(x) > 0 ,map(lambda x: x.strip("/"), path.split('/')))

        for item in identifiers:
          if item == '..':
            if len(q) > 0:
              q.pop()
          else:
            q.append(item)

        return f"/{'/'.join(q)}"
