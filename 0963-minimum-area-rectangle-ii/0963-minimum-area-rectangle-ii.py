class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
      points_set = set(map(tuple, points))
      output = inf
      seen_rects = set()

      for i in range(len(points)):
          for j in range(len(points)):
              for k in range(len(points)):
                  if i == j or i == k or j == k:
                      continue
                  A = tuple(points[i])
                  B = tuple(points[j])
                  C = tuple(points[k])
                  
                  v1 = (B[0] - A[0], B[1] - A[1])
                  v2 = (C[0] - A[0], C[1] - A[1])
                  dot = v1[0]*v2[0] + v1[1]*v2[1]
                  if dot != 0:
                      continue

                  D = (B[0] + C[0] - A[0], B[1] + C[1] - A[1])
                  if D not in points_set:
                      continue

                  rect = frozenset([A, B, C, D])
                  if rect in seen_rects:
                      continue
                  seen_rects.add(rect)

                  side1 = sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
                  side2 = sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)
                  area = side1 * side2
                  output = min(output, area)

      return 0 if output == inf else output