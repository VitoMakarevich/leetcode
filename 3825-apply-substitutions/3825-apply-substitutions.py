class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
      self._replacements = dict(replacements)
      return self.resolve_text(text)
    
    @cache
    def get_replacement(self, key):
      raw_value = self._replacements[key]
      return self.resolve_text(raw_value)
      
      
    def resolve_text(self, value):
      parts = value.split('%')
      res = StringIO()
      for i, part in enumerate(parts):
        if i % 2 == 1:
          ready_part = self.get_replacement(part)
        else:
          ready_part = part
        res.write(ready_part)
      return res.getvalue()

