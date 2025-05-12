class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
          return False
        target_size = len(s1)
        target_map = Counter(s1)

        current_counter = Counter()
        left = 0
        right = 0
        while right < len(s2):
          if right - target_size >= 0:
            leftmost_char = s2[right - target_size]
            current_counter[leftmost_char] -= 1
            if current_counter[leftmost_char] == 0:
              del current_counter[leftmost_char]
          
          
          current_counter[s2[right]] += 1
          if current_counter == target_map:
              return True
          right += 1
        return False