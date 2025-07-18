class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
      ltr = self.fix(s, '(', ')')
      rtl = self.fix(ltr[::-1], ')', '(')
      return rtl[::-1]
    
    def fix(self, s, open_ch, close_ch):
      opened = 0
      res = ''
      for char in s:
        if char == open_ch:
          opened += 1
          res += char
        elif char == close_ch:
          if opened > 0:
            opened -= 1
            res += char
        else:
          res+=char
      return res  
        
            
        