class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)
        heap = []
        for number, occurences in counter.items():
            heapq.heappush(heap, (-occurences, number))
        
        res = []
        for i in range(k):
            occurences, number = heapq.heappop(heap)
            res.append(number)

        return res

