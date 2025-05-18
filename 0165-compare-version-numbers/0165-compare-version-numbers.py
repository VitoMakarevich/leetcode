class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
      v1, v2 = self.normalize(version1), self.normalize(version2)
      min_l = min(len(v1), len(v2))
      for i in range(min_l):
        if v1[i] < v2[i]:
          return -1
        elif v1[i] > v2[i]:
          return 1
      if len(v1) == len(v2):
        return 0
      
      remain_v1, remain_v2 = v1[min_l:], v2[min_l:]
      if any(remain_v1):
        return 1
      elif any(remain_v2):
        return -1
      return 0

    def normalize(self, v):
      return list(map(int, v.split('.')))