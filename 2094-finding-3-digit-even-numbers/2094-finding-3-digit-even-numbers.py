class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            num, c = divmod(num, 10)
            a, b = divmod(num, 10)
            freq[a] -= 1
            freq[b] -= 1
            freq[c] -= 1
            if freq[a] >= 0 and freq[b] >= 0 and freq[c] >= 0:
                res.append(a * 100 + b * 10 + c)
            freq[a] += 1
            freq[b] += 1
            freq[c] += 1
        return res
            