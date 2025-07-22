class Solution:
    def maximumLength(self, nums: List[int]) -> int:
      remains = [num % 2 for num in nums]
      
      
      def changing_start_from(search):
        counter = 0
        for n in remains:
          if n == search:
            counter += 1
            search = int(not bool(search))
            print(search)
        return counter
      res = max(changing_start_from(0), changing_start_from(1), sum(1 for n in remains if n == 1), sum([0 for n in remains if n == 0]))
      return res
    