class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
    
      palindrome_pairs = defaultdict(int)
      palindrome_pair_count = 0
      palindrome_single = 0
      for word in words:
        reverse = word[::-1]
        if palindrome_pairs[reverse] > 0:
          palindrome_pair_count += 4
          palindrome_pairs[reverse] -= 1
        else:
          palindrome_pairs[word] += 1
      for cand, count in palindrome_pairs.items():
        if cand == cand[::-1] and count > 0:
          return palindrome_pair_count + 2
      return palindrome_pair_count
