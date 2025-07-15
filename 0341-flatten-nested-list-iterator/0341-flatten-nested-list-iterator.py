# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
      self._iterable = []
      self._idx = 0
      self._flatten(nestedList)
      
    def next(self) -> int:
      res = self._iterable[self._idx]
      self._idx += 1
      return res
    
    def hasNext(self) -> bool:
      return self._idx < len(self._iterable)

    def _flatten(self, nestedList):
      for ni in nestedList:
        if ni.isInteger():
          self._iterable.append(ni.getInteger())
        else:
          self._flatten(ni.getList())

        
        
    
    


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())