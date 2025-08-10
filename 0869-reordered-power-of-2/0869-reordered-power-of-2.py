def calc_powers_of_2():
  max_n = 10 ** 9
  powers_of_2 = set()
  cur = 1
  while cur <= max_n:
    cur_str = tuple(sorted(list(str(cur))))
    powers_of_2.add(cur_str)
    cur <<= 1
  return powers_of_2

powers_of_2 = calc_powers_of_2()

class Solution:
  def reorderedPowerOf2(self, n: int) -> bool:
    return tuple(sorted(list(str(n)))) in powers_of_2