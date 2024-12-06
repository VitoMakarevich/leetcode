class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
      aux = [0] * len(logs)
      mapped = list(map(LogItem, logs))
      sorted_arr = self._sort(mapped, aux)
      res = list(map(lambda x: x._l, sorted_arr))
      return res

    def _sort(self, arr_to_sort, aux):
      if len(arr_to_sort) > 1:
        mid = len(arr_to_sort) // 2
        left = self._sort(arr_to_sort[:mid], aux)
        right = self._sort(arr_to_sort[mid:], aux)
        return self._merge(left, right)
      else:
        return arr_to_sort

    def _merge(self, left, right):
        left_ptr = 0
        right_ptr = 0
        res = 0
        merged = []
        while left_ptr < len(left) and right_ptr < len(right):
          l_cand = left[left_ptr]
          r_cand = right[right_ptr]
          
          cmp_res = self._compare(l_cand, r_cand)
          # print(f"for {l_cand._l} and {r_cand._l} res is {cmp_res}")
          if cmp_res <= 0:
            merged.append(l_cand)
            left_ptr += 1
          else:
            merged.append(r_cand)
            right_ptr += 1
          res += 1
        merged.extend(left[left_ptr:])
        merged.extend(right[right_ptr:])
        return merged

    def _compare(self,left, right):
      if not left._is_letter and not right._is_letter:
        return -1
      elif left._is_letter and not right._is_letter:
        return -1
      elif not left._is_letter and right._is_letter:
        return 1
      else:
        text_equals = self._compare_strings(left._remain, right._remain)
        if not text_equals == 0:
          return text_equals
        return self._compare_strings(left._identifier, right._identifier)

    def _compare_strings(self, str1, str2):
      if str1 < str2:
          return -1
      elif str1 > str2:
          return 1
      else:
          return 0


class LogItem:
  def __init__(self, l):
    parts = l.split(' ')
    self._identifier = parts[0]
    self._l = l
    self._remain = '9'.join(parts[1:])
    self._is_letter = False
    for c in self._remain:
      if not c.isdigit():
        self._is_letter = True
        break

    

