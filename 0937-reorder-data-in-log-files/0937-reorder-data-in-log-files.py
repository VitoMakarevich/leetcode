class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
      aux = [0] * len(logs)
      mapped = list(map(LogItem, logs))
      self._sort(mapped, aux, 0 , len(logs) - 1)
      res = list(map(lambda x: x._l, mapped))
      return res

    def _sort(self, arr_to_sort, aux, low, high):

      if low < high:
        mid = (low + high) // 2
        self._sort(arr_to_sort, aux, low, mid)
        self._sort(arr_to_sort, aux, mid + 1, high)
        self._merge(arr_to_sort, aux, low, mid, high)
      return arr_to_sort

    def _merge(self, arr, aux, low, mid, high):
        for i in range(low, high + 1):
          aux[i] = arr[i]
        left_ptr = low
        right_ptr = mid + 1
        res = low
        while left_ptr <= mid and right_ptr <= high:
          l_cand = aux[left_ptr]
          r_cand = aux[right_ptr]
          
          cmp_res = self._compare(l_cand, r_cand)
          if cmp_res <= 0:
            arr[res] = l_cand
            left_ptr += 1
          else:
            arr[res] = r_cand
            right_ptr += 1
          res += 1
        while left_ptr <= mid:
          arr[res] = aux[left_ptr]
          left_ptr += 1
          res += 1
        while right_ptr <= high:
          arr[res] = aux[right_ptr]
          right_ptr += 1
          res += 1

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

    

