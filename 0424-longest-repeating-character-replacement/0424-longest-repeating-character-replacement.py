class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = l = 0
        count = collections.Counter() # counting the occurance of the character in the string. 
		# instead of using "count = collections.Counter()", we can do the following:-
		
        for r in range(len(s)):
            count[s[r]] += 1 # increasing the count of the character as per its occurance. 
            maxf = max(maxf, count[s[r]]) # having a max freq of the character that is yet occurred. 
            if r - l + 1 > maxf + k:  # if length of sliding window is greater than max freq of the character and the allowed number of replacement.
                count[s[l]] -= 1 # then we have to decrease the occurrance of the character by 1 are we will be sliding the window. 
                l += 1 # and we have to slide our window
        return len(s) - l  # this will provide the length of the longest substring containing the same letter with the replacement allowed. 