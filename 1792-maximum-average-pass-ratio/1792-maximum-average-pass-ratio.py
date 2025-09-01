class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
      current_ratio = []
      for passed, total in classes:
        current_rate = passed / total
        potential_rate = (passed + 1) / (total + 1)
        current_ratio.append((-(potential_rate - current_rate), passed, total, potential_rate))
      heapq.heapify(current_ratio)

      for e in range(extraStudents):
        _, passed, total, rate = heapq.heappop(current_ratio)
        passed += 1
        total += 1
        new_potential = (passed + 1) / (total + 1)
        heapq.heappush(current_ratio, (-(new_potential - rate), passed, total, new_potential))
        
      
      return sum([passed / total for _, passed, total, _ in current_ratio]) / len(classes)