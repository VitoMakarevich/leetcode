from io import StringIO
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       buffer = StringIO()
       l1, l2 = len(word1), len(word2)
       i, j = 0, 0
       while i < l1 and j < l2:
         buffer.write(word1[i])
         buffer.write(word2[j])
         i += 1
         j += 1
       buffer.write(word1[i:])
       buffer.write(word2[j:])
       return buffer.getvalue()  
